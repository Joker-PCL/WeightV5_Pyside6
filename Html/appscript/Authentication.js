/*
--validateToken
  --getCookie
    --isTrue(setCookie)
    --isFalse(userProperties.deleteProperty('header'))
*/

// เข้ารหัส SHA-256
function sha256(password) {
  var digest = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, password, Utilities.Charset.UTF_8);
  var hashedPassword = '';
  for (var i = 0; i < digest.length; i++) {
    var byte = digest[i];
    hashedPassword += (byte < 0x10 ? '0' : '') + (byte & 0xFF).toString(16);
  }
  return hashedPassword;
}

// ดึงข้อมูลผู้ใช้จาก Properties Service
function getCookie() {
  const userProperties = PropertiesService.getUserProperties();
  const headerDataString = userProperties.getProperty('header');
  const header = JSON.parse(headerDataString);

  const headerBase64 = header["Authorization"];
  const headerBase64deCode = Utilities.newBlob(Utilities.base64Decode(headerBase64)).getDataAsString();
  const [jsonWebToken, privateKey] = headerBase64deCode.split(":");
  console.log(jsonWebToken, privateKey)
  return { jsonWebToken, privateKey };
}

// ส่งข้อมูลผู้ใช้ผ่าน Properties Service
function setCookie(jsonWebToken, privateKey) {
  const userProperties = PropertiesService.getUserProperties();
  const header = {
    "Authorization": Utilities.base64Encode(`${jsonWebToken}:${privateKey}`)
  }

  userProperties.setProperty('header', JSON.stringify(header));
}

// เคลียร์ข้อมูลผู้ใช้ผ่าน Properties Service
function clearCookie() {
  const userProperties = PropertiesService.getUserProperties();
  userProperties.deleteAllProperties();
}

// สร้าง Token parameter(privateKey, หมดอายุภายในชั่วโมง, ข้อมูลผู้ใช้งาน)
const createJWT = ({ privateKey, expiresInHours, data = {} }) => {
  // Header
  const header = {
    alg: 'HS256',
    typ: 'JWT',
  };

  // Payload
  const now = Date.now();
  const expires = new Date(now);
  expires.setHours(expires.getHours() + expiresInHours);
  const payload = {
    exp: Math.round(expires.getTime() / 1000),
    iat: Math.round(now / 1000),
  };

  // Add user data to payload
  Object.assign(payload, data);

  // Function to encode text to base64
  const base64Encode = (text) => {
    return Utilities.base64EncodeWebSafe(text).replace(/=+$/, '');
  };

  // Combine header and payload, then encode to base64
  const encodedHeader = base64Encode(JSON.stringify(header));
  const utf8EncodedPayload = Utilities.newBlob(JSON.stringify(payload)).getBytes();
  const encodedPayload = base64Encode(utf8EncodedPayload);
  const toSign = `${encodedHeader}.${encodedPayload}`;

  // Compute HMAC SHA-256 signature
  const signatureBytes = Utilities.computeHmacSha256Signature(toSign, privateKey);
  const signature = Utilities.base64EncodeWebSafe(signatureBytes).replace(/=+$/, '');

  // Return JWT
  return `${toSign}.${signature}`;
}

// สร้าง Token parameter(privateKey, ชื่อภาษาไทย)
const generateAccessToken = ({ privateKey, data = {} }) => {
  const accessToken = createJWT({
    privateKey,
    expiresInHours: 6, // expires in 6 hours
    data
  });

  return accessToken;
}

// ตรวจสอบความถูกต้องของ Token
const validateToken = () => {
  try {
    const {jsonWebToken, privateKey} = getCookie();

    if (jsonWebToken && privateKey) {
      const [header, payload, signature] = jsonWebToken.split('.');
      const signatureBytes = Utilities.computeHmacSha256Signature(`${header}.${payload}`, privateKey);
      const validSignature = Utilities.base64EncodeWebSafe(signatureBytes);
      if (signature === validSignature.replace(/=+$/, '')) {
        const blob = Utilities.newBlob(Utilities.base64Decode(payload)).getDataAsString();
        const { exp, ...data } = JSON.parse(blob);
        if (new Date(exp * 1000) > new Date()) {
          const newJsonWebToken = generateAccessToken({ privateKey, data });
          setCookie(newJsonWebToken, privateKey);
          return { 
            message: 'success',
            jsonWebToken: newJsonWebToken,
            data: data 
          };
        }
        else {
          return { message: 'the token has expired' };
        }
      } else {
        return { message: 'the token has expired' };
      }
    }
    else {
      return { message: 'invalid Signature' };
    }
  }
  catch (error) {
    return { message: error.message }; // แสดงข้อความ error ที่เกิดขึ้น
  }
}

// ทดสอบ JWT
function testGenerateAccessToken() {
  const privateKey = '819e3d6c1381eac87c17617e5165f38c';
  const data = {
    nameEN: "Nattapon",
    nameTH: "ณัฐพล",
    role: "Admin",
  }

  const token = generateAccessToken({ privateKey, data });

  setCookie(token, privateKey);
}

function testParseJwt() {
  const result = validateToken();
  console.log(result)
}

function testSHA256() {
  var password = "2077"; // แทนรหัสผ่านที่ต้องการแปลงที่นี่
  var hashedPassword = sha256(password);
  Logger.log("รหัสผ่านที่แปลงเป็นรูปแบบ SHA-256: " + hashedPassword);
}

function testPDF() {
  // https://drive.google.com/file/d/1zDep-HhPul4PfJMEyJ2ZEeSc1SSgEiLX/view?usp=drive_link
  var fileId = '16vtrC4ofFc3_lrwqkxmNi3gLI-V1OG78ZXE9kIWqk0A'; // แทนที่ด้วย ID ของไฟล์ PDF ที่ต้องการ
  var file = DriveApp.getFileById(fileId);
  var pdfUrl = file.getDownloadUrl();

  console.log(pdfUrl);
}

