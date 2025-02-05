import { useState, useEffect } from "react";
import "./App.css";

function RemoveBG() {
  // api key dapat dri remove bg API
  const apiKey = import.meta.env.VITE_API_KEY;
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [fileName, setFileName] = useState("");

  // Bersihkan URL saat komponen unmount
  useEffect(() => {
    return () => {
      if (result && !result.startsWith("Error")) {
        URL.revokeObjectURL(result);
      }
    };
  }, [result]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const input = e.target.elements.input;

    if (!input.files || !input.files[0]) {
      setResult("Error: Please select an image file");
      return;
    }

    // Simpan nama file
    setFileName(input.files[0].name.split(".")[0]);

    setLoading(true);
    const formData = new FormData();
    formData.append("image_file", input.files[0]);

    try {
      const response = await fetch(`https://api.remove.bg/v1.0/removebg`, {
        method: "POST",
        headers: {
          "X-Api-Key": apiKey,
        },
        body: formData,
      });

      if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        setResult(url);
      } else {
        setResult("Error: " + (await response.text()));
      }
    } catch (error) {
      setResult("Error:" + error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = async () => {
    try {
      const response = await fetch(result);
      const blob = await response.blob();

      const downloadImg = document.createElement("a");
      downloadImg.href = URL.createObjectURL(blob);
      downloadImg.download = `${fileName}-no-bg.png`;

      document.body.appendChild(downloadImg);
      downloadImg.click();
      document.body.removeChild(downloadImg);

      // Bersihkan URL object
      URL.revokeObjectURL(downloadImg.href);
    } catch (error) {
      console.error("Download error:", error);
    }
  };

  return (
    <>
      <header>
        <h1>Remove Background</h1>
      </header>
      <main className="card">
        <form onSubmit={handleSubmit}>
          <input type="file" id="input" accept="image/*" />
          <button type="submit" disabled={loading}>
            {loading ? "Processing..." : "Remove"}
          </button>
        </form>
        {loading && <p>Processing image...</p>}
        {result && (
          <div id="result">
            {result.startsWith("Error") ? (
              <p>{result}</p>
            ) : (
              <div>
                <img
                  src={result}
                  alt="Processed image"
                  className="img-result"
                />
                <button onClick={handleDownload} className="download-btn">
                  Download Image
                </button>
              </div>
            )}
          </div>
        )}
      </main>
    </>
  );
}

export default RemoveBG;
