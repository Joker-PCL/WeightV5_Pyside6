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

// สร้าง Token parameter(privateKey, หมดอายุภายในชั่วโมง, ข้อมูลผู้ใช้งาน)
const createJWT = ({ privateKey, expiresInHours, userData = {} }) => {
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
  Object.assign(payload, userData);

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

// สร้าง Token parameter(privateKey, ข้อมูลผู้ใช้งาน)
const generateAccessToken = ({ privateKey, userData = {} }) => {
  const accessToken = createJWT({
    privateKey,
    expiresInHours: 6, // expires in 6 hours
    userData
  });

  return Utilities.base64Encode(`${accessToken}:${privateKey}`);
}

// ตรวจสอบความถูกต้องของ Token
const validateToken = (jsonWebToken) => {
  try {
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = spreadsheet.getSheetByName(globalVariables().shUserLists);
    const dataLists = sheet.getDataRange().getDisplayValues().slice(2);

    const headerBase64deCode = Utilities.newBlob(Utilities.base64Decode(jsonWebToken)).getDataAsString();
    const [jwt, privateKey] = headerBase64deCode.split(":");

    if (jwt && privateKey) {
      const [header, payload, signature] = jwt.split('.');
      const signatureBytes = Utilities.computeHmacSha256Signature(`${header}.${payload}`, privateKey);
      const validSignature = Utilities.base64EncodeWebSafe(signatureBytes);
      if (signature === validSignature.replace(/=+$/, '')) {
        const blob = Utilities.newBlob(Utilities.base64Decode(payload)).getDataAsString();
        const { exp, ...userData } = JSON.parse(blob);
        if (new Date(exp * 1000) > new Date()) {
          const searchUserdata = dataLists.find((dataList) => {
            const _nameTH = dataList[2];
            const _searchPrivateKey = dataList[4];
            const _role = dataList[5];
            return _nameTH == userData.nameTH && (_searchPrivateKey == privateKey && _role == userData.role);
          });

          if(searchUserdata) {
            const newJsonWebToken = generateAccessToken({ privateKey, userData });
            return {
              "message": 'success',
              "jsonWebToken": newJsonWebToken,
              "userData": userData
            };
          }
          else {
            return { message: 'The session has expired' };
          }
        }
        else {
          return { message: 'The token has expired' };
        }
      } else {
        return { message: 'The token has expired' };
      }
    }
    else {
      return { message: 'Invalid Signature' };
    }
  }
  catch (error) {
    return { message: error.message }; // แสดงข้อความ error ที่เกิดขึ้น
  }
}

// ทดสอบ JWT
function testGenerateAccessToken() {
  const privateKey = '819e3d6c1381eac87c17617e5165f38c';
  const userData = {
    nameEN: "Nattapon",
    nameTH: "ณัฐพล",
    role: "Admin",
  }

  const token = generateAccessToken({ privateKey, userData });
  console.log(token)
}

function testParseJwt() {
  const result = validateToken("ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmxlSEFpT2pFM01UVXdOakUzTnpNc0ltbGhkQ0k2TVRjeE5UQTBNREUzTXl3aWJtRnRaVVZPSWpvaVRtRjBkR0Z3YjI0aUxDSnVZVzFsVkVnaU9pTGd1SlBndUxIZ3VKRGd1SjdndUtVaUxDSnliMnhsSWpvaVFXUnRhVzRpZlEuYzl6VFFwTmRkVkxYbU41enYxbjk1ZG9LZC1uRWtucjQ0R1kxelQ0c1UwTTo4MTllM2Q2YzEzODFlYWM4N2MxNzYxN2U1MTY1ZjM4Yw==");
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

