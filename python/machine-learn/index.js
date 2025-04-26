const axios = require('axios');
 
// Fungsi untuk menghasilkan nomor HP random dengan format 851-XXXX-XXXX
const generateRandomPhoneNumber = () => {
const randomPart1 = Math.floor(1000 + Math.random() * 9000); // 4 digit
const randomPart2 = Math.floor(1000 + Math.random() * 9000); // 4 digit
return `851-${randomPart1}-${randomPart2}`;
};
 
const fetchData = async () => {
const randomPhoneNumber = generateRandomPhoneNumber();
 
try {
const response = await axios.post(
'https://gojek-kartu-fisik.enhost.top/req/b.php',
new URLSearchParams({ nohp: randomPhoneNumber }), // Data payload dengan nomor acak
{
headers: {
'sec-ch-ua-platform': '"Windows"',
'Referer': 'https://gojek-kartu-fisik.enhost.top/b.php',
'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
'sec-ch-ua-mobile': '?0',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
'Accept': 'text/plain, */*; q=0.01',
'DNT': '1',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'PHPSESSID=c48542d30bc5497768e2fc693c2d0a66'
}
}
);
 
console.log('Random No HP:', randomPhoneNumber); // Print nomor HP yang dikirim
console.log('Response Code:', response.status); // Print HTTP status code
console.log('Response Data:', response.data); // Print response data
} catch (error) {
console.error('Error fetching data:', error.response ? error.response.status : error.message);
}
};
 
// Jalankan fetchData setiap 2 detik dengan nomor HP random
setInterval(fetchData, 2000);