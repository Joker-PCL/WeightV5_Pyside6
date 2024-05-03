// ตั้งค่า
function globalVariables() {
  const Variables = {
    // icon https://pic.in.th/
    icon: "https://img5.pic.in.th/file/secure-sv1/table-of-content.png",

    // MetaTag
    metaTag06: [
      "viewport",
      "width=device-width, height=device-height,initial-scale=0.6, minimum-scale=0.6, maximum-scale=0.6",
    ],
    metaTag08: [
      "viewport",
      "width=device-width, height=device-height,initial-scale=0.8, minimum-scale=0.8, maximum-scale=0.8",
    ],
    // Shortened links
    shortenedLinks: "https://bit.ly/WeightTableV4",
    // Line jsonWebToken
    alert_token: "p9YWBiZrsUAk7Ef9d0hLTMMF2CxIaTnRopHaGcosM4q",
    approval_token: "lYlhqcenm4d8Vq4VJOYO2T8VHh0tbaW7oSrsJU9tm7f",

    // แฟ้มข้อมูลเวอร์ชั่นเก่า
    folderIdIPC_OLD: "1RJx8vxspQTJR05GaTLtLqm1kBtfQYC0W",
    folderId10s_OLD: "10JT2s9zd8pcmSj-kB2T5s-kFHlW58IE3",

    // ข้อมูลใน Main_Setup
    shUserList: "User_Password", // ชีตข้อมูลรายชื่อพนักงาน
    shTabetList: "TabletID", // ข้อมูล url เครื่องตอก
    shScaleList: "ScaleID", // ชีตข้อมูลเครื่องชั่ง
    shProductNameList: "ProductNameList", // ชีตข้อมูลรายชื่อยา
    shAudit_log: "Audit_Log", // ชีต audit trail

    shRemarks: "Remark", // ชีต Remarks
    shSetWeight: "Setting", // ชีต ข้อมูลการตั้งค่าน้ำหนัก

    // ข้อมูลของระบบชั่ง 10 เม็ด
    folderId10s: "1J7jfGUshmFox9RHK2cqfvCGTaQcncOKx", // ID โฟล์เดอร์แฟ้มข้อมูลน้ำหนัก 10 เม็ด
    inspectorCol: 7, // คลอลั่มลงชื่อผู้ตรวจสอบ
    shWeight10s: "WEIGHT", // ข้อมูลน้ำหนัก 10 เม็ด
    setupRange10s: "B2:B17", // ตำแหน่ง ข้อมูลการตั้งค่าน้ำหนัก 10 เม็ด
    preparedRange10s: "B14", // ตำแหน่ง ลงชื่อการตั้งค่าน้ำหนัก 10 เม็ด
    approvedRange10s: "B15", // ตำแหน่ง ลงชื่อตรวจสอบการตั้งค่าน้ำหนัก 10 เม็ด
    finished10s: "B16", // ตำแหน่ง ลงชื่อจบการผลิต น้ำหนัก 10 เม็ด
    finishTime10s: "B17", // ตำแหน่ง ลงเวลาจบการผลิต น้ำหนัก 10 เม็ด

    // ข้อมูลระบบชั่ง IPC
    folderIdIPC: "1qtpt0eAp_IOWe1BEh-x75nM5FXNy9tdW", // ID โฟล์เดอร์แฟ้มข้อมูล IPC
    shWeightIPC: "Weight", // ข้อมูลน้ำหนัก IPC
    setupRangeIPC: "B2:B19", // ตำแหน่ง ข้อมูลการตั้งค่าน้ำหนัก IPC
    preparedRangeIPC: "B16", // ตำแหน่ง ลงชื่อการตั้งค่าน้ำหนัก IPC
    approvedRangeIPC: "B17", // ตำแหน่ง ลงชื่อตรวจสอบการตั้งค่าน้ำหนัก IPC
    finished10s: "B18", // ตำแหน่ง ลงชื่อจบการผลิต น้ำหนัก IPC
    finishTime10s: "B19", // ตำแหน่ง ลงเวลาจบการผลิต น้ำหนัก IPC
  };

  return Variables;
}

function doGet(e) {
  let htmlOutput = HtmlService.createTemplateFromFile("index");
  return htmlOutput
    .evaluate()
    .setFaviconUrl(globalVariables().icon)
    .addMetaTag(...globalVariables().metaTag06)
    .setTitle("Weight Table")
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

// ********* ลงชื่อเข้าใช้งาน ********* \\
function login(form) {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = spreadsheet.getSheetByName(globalVariables().shUserList);
  const dataLists = sheet.getDataRange().getDisplayValues().slice(2);

  if (form.username && form.password) {
    const results = dataLists.find((dataList) => {
      const _username = dataList[2];
      return _username == form.username;
    });

    if (results) {
      const privateKey = sha256(`${form.password}`);
      const [_rfid, _id, _nameTH, _nameEN, _privateKey, _role] = results;
      const userData = {
        nameTH: _nameTH,
        nameEN: _nameEN,
        role: _role,
      };

      if (_privateKey == privateKey) {
        const jsonWebToken = generateAccessToken({ privateKey, userData });
        return { message: "success", jsonWebToken: jsonWebToken, userData: userData };
      } else {
        return { message: "password is incorrect!" };
      }
    } else {
      return { message: "no user information found!!" };
    }
  }
}

// ********* ส่งไลน์ ********* \\
function sendLineNotify(message, jsonWebToken) {
  if (!jsonWebToken) {
    jsonWebToken = globalVariables().alert_token;
  }

  var options = {
    method: "post",
    payload: "message=" + message,
    headers: {
      Authorization: "Bearer " + jsonWebToken,
    },
  };

  UrlFetchApp.fetch("https://notify-api.line.me/api/notify", options);
}

function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

function getUrl() {
  const url = ScriptApp.getService().getUrl();
  return url;
}
