// ตั้งค่า DataTable
const setupTable = {
  // กำหนดเมนูแสดงจำนวนแถว
  lengthMenu: [
    [5, 10, 15, 20, 50, 100, -1],
    ["5", "10", "15", "20", "50", "100", "ทั้งหมด"],
  ],

  // columnDefs: [
  //     { "orderable": false, "targets": [1, 2, 3, 4, 5, 6] },
  // ],

  // ordering: false,
  order: [[0, "desc"]],
  iDisplayLength: 10,
  responsive: true,

  //ภาษาไทย
  language: {
    sLengthMenu: "แสดง _MENU_ รายการ",
    sZeroRecords: "ไม่พบข้อมูล",
    sInfo: "แสดง _START_ ถึง _END_ จาก _TOTAL_ รายการ",
    sInfoEmpty: "แสดง 0 ถึง 0 จาก 0 รายการ",
    sInfoFiltered: "(กรองข้อมูลจาก _MAX_ รายการ)",
    sInfoPostFix: "",
    sSearch: "ค้นหา:",
    sUrl: "",
    oPaginate: {
      sFirst: "หน้าแรก",
      sPrevious: "ก่อนหน้า",
      sNext: "ถัดไป",
      sLast: "หน้าสุดท้าย",
    },
  },
};

// ข้อมูลการชั่ง 10 เม็ด
const dataUpdate = {
  settingDetail: {
    productName: "ASCOT 88888",
    lot: "32219R",
    balanceID: "PI-229",
    tabletID: "T11",
    meanWeight: "0.98",
    percentWeightVariation: "3.00%",
    meanWeightMin: "0.96",
    meanWeightMax: "1.00",
    meanWeightRegMin: "0.89",
    meanWeightRegMax: "1.07",
    thicknessMin: "2.50",
    thicknessMax: "2.90",
    prepared: "อรทัย",
    approved: "xxxxx",
    finished: "xxxxx",
    finishTime: "xxxxx",
  },

  // ข้อมูลการชั่งน้ำหนัก 10 เม็ด
  weighing: {
    dataset: {
      "01/02/2024, 19:57:58": {
        type: "ONLINE",
        weight1: "0.959",
        weight2: "1.001",
        characteristics: "ผิดปกติ",
        operator: "สะกุณา",
        inspector: "ชิตชนก",
        thickness: {
          thickness1: "2.80",
          thickness2: "2.75",
          thickness3: "2.49",
          thickness4: "2.76",
          thickness5: "3.80",
          thickness6: "2.75",
          thickness7: "2.79",
          thickness8: "2.76",
          thickness9: "2.91",
          thickness10: "2.78",
        },
      },
    },
  },

  // Remarks
  remarks: {
    dataset: {
      "01/02/2024, 12:55:49": {
        issues: "[แจ้งเตือนจากระบบ]\n เหตุการที่เกิดการเปลี่ยนแปลง",
        cause: "ทดสอบ, สาเหตุ",
        resolve: "ทดสอบ, การแก้ไข",
        notes: "ทดสอบ, หมายเหตุ",
        recorder: "ทดสอบ, ผู้บันทึก",
        role: "Admin",
      },
    },
  },
};

// ข้อมูลการชั่ง 10 เม็ด
const datatest = {
  settingDetail: {
    productName: "ASCOT 81",
    lot: "32219R",
    balanceID: "PI-229",
    tabletID: "T11",
    meanWeight: "0.98",
    percentWeightVariation: "3.00%",
    meanWeightMin: "0.96",
    meanWeightMax: "1.00",
    meanWeightRegMin: "0.89",
    meanWeightRegMax: "1.07",
    thicknessMin: "2.50",
    thicknessMax: "2.90",
    prepared: "อรทัย",
    approved: "สิริยาภรณ์",
    finished: "xxxxx",
    finishTime: "xxxxx",
  },

  // ข้อมูลการชั่งน้ำหนัก 10 เม็ด
  weighing: {
    dataset: {
      "01/02/2024, 19:57:58": {
        type: "ONLINE",
        weight1: "0.959",
        weight2: "1.001",
        characteristics: "ผิดปกติ",
        operator: "สะกุณา",
        inspector: "ชิตชนก",
        thickness: {
          thickness1: "2.80",
          thickness2: "2.75",
          thickness3: "2.49",
          thickness4: "2.76",
          thickness5: "3.80",
          thickness6: "2.75",
          thickness7: "2.79",
          thickness8: "2.76",
          thickness9: "2.91",
          thickness10: "2.78",
        },
      },
    },
  },

  // Remarks
  remarks: {
    dataset: {
      "01/02/2024, 12:55:49": {
        issues: "ทดสอบ,เหตุการที่เกิดการเปลี่ยนแปลง",
        cause: "ทดสอบ, สาเหตุ",
        resolve: "ทดสอบ, การแก้ไข",
        notes: "ทดสอบ, หมายเหตุ",
        recorder: "ทดสอบ, ผู้บันทึก",
        role: "Admin",
      },
      "31/03/2024, 02:55:14": {
        issues:
          "น้ำหนักไม่ได้อยู่ในช่วงที่กำหนด \nช่วงที่กำหนด \n(0.970g. - 1.030g.) \nน้ำหนักที่ชั่ง \n['1.006', '2.004'] \nค่าเฉลี่ยที่ได้ 1.505g.",
        cause: "พนักงานลืมกด  re-zero ของเครื่องชั่งในการชั่งน้ำหนักรอบที่2",
        resolve:
          "นำเม็ดยายาชุดเดิมมาชั่งใหม่ในเวลา 03:00 น. ครั้งที่1 \n 0.999 กรัม ครั้งที่2 1.001 g ค่าอยู่ในเกณฑ์การยอมรับผลิตจึงนำไปผลิตต่อ",
        notes: "",
        recorder: "ชิตชนก",
        role: "Superuser",
      },
    },
  },
};

// ข้อมูลการชั่ง ipc
const datatestIpc = {
  settingDetail: {
    productName: "ASCOT 81",
    lot: "40545R",
    balanceID: "PI-229",
    tabletID: "T11",
    numberPunches: "25",
    numberTablets: "30",
    meanWeight: "0.100",
    percentWeightVariation: "8.00%",
    meanWeightAvgMin: "0.097",
    meanWeightAvgMax: "0.103",
    meanWeightInhouseMin: "0.092",
    meanWeightInhouseMax: "0.107",
    meanWeightRegMin: "0.090",
    meanWeightRegMax: "0.107",
    prepared: "อรทัย",
    approved: "สิริยาภรณ์",
    finished: "xxxxx",
    finishTime: "xxxxx",
  },

  // ข้อมูลการชั่งน้ำหนัก 10 เม็ด
  weighing: {
    dataset: {
      "21/03/2024, 23:31:03": {
        operator: "Prayut",
        type: "OFFLINE",
        characteristics: "ผิดปกติ",
        weights: {
          "No.1": { timestamp: "23:30:00", weight: "0.105" },
          "No.2": { timestamp: "23:30:02", weight: "0.083" },
          "No.3": { timestamp: "23:30:04", weight: "0.110" },
          "No.4": { timestamp: "23:30:06", weight: "0.086" },
          "No.5": { timestamp: "23:30:08", weight: "0.112" },
          "No.6": { timestamp: "23:30:10", weight: "0.092" },
          "No.7": { timestamp: "23:30:12", weight: "0.108" },
          "No.8": { timestamp: "23:30:14", weight: "0.080" },
          "No.9": { timestamp: "23:30:16", weight: "0.101" },
          "No.10": { timestamp: "23:30:18", weight: "0.114" },
          "No.11": { timestamp: "23:30:20", weight: "0.085" },
          "No.12": { timestamp: "23:30:22", weight: "0.093" },
          "No.13": { timestamp: "23:30:24", weight: "0.111" },
          "No.14": { timestamp: "23:30:26", weight: "0.087" },
          "No.15": { timestamp: "23:30:28", weight: "0.107" },
          "No.16": { timestamp: "23:30:30", weight: "0.081" },
          "No.17": { timestamp: "23:30:32", weight: "0.100" },
          "No.18": { timestamp: "23:30:34", weight: "0.115" },
          "No.19": { timestamp: "23:30:36", weight: "0.084" },
          "No.20": { timestamp: "23:30:38", weight: "0.094" },
          "No.21": { timestamp: "23:30:40", weight: "0.109" },
          "No.22": { timestamp: "23:30:42", weight: "0.082" },
          "No.23": { timestamp: "23:30:44", weight: "0.096" },
          "No.24": { timestamp: "23:30:46", weight: "0.113" },
          "No.25": { timestamp: "23:30:48", weight: "0.088" },
          "No.26": { timestamp: "23:30:50", weight: "0.106" },
          "No.27": { timestamp: "23:30:52", weight: "0.079" },
          "No.28": { timestamp: "23:30:54", weight: "0.102" },
          "No.29": { timestamp: "23:30:56", weight: "0.116" },
          "No.30": { timestamp: "23:30:58", weight: "0.090" },
        },
      },
      "20/03/2024, 23:53:05": {
        operator: "Prayut",
        type: "ONLINE",
        characteristics: "ปกติ",
        weights: {
          "No.1": { timestamp: "23:52:01", weight: "0.108" },
          "No.2": { timestamp: "23:52:03", weight: "0.087" },
          "No.3": { timestamp: "23:52:05", weight: "0.102" },
          "No.4": { timestamp: "23:52:07", weight: "0.092" },
          "No.5": { timestamp: "23:52:09", weight: "0.113" },
          "No.6": { timestamp: "23:52:11", weight: "0.096" },
          "No.7": { timestamp: "23:52:13", weight: "0.081" },
          "No.8": { timestamp: "23:52:15", weight: "0.109" },
          "No.9": { timestamp: "23:52:17", weight: "0.110" },
          "No.10": { timestamp: "23:52:19", weight: "0.114" },
          "No.11": { timestamp: "23:52:21", weight: "0.085" },
          "No.12": { timestamp: "23:52:23", weight: "0.091" },
          "No.13": { timestamp: "23:52:25", weight: "0.104" },
          "No.14": { timestamp: "23:52:27", weight: "0.097" },
          "No.15": { timestamp: "23:52:29", weight: "0.115" },
          "No.16": { timestamp: "23:52:31", weight: "0.083" },
          "No.17": { timestamp: "23:52:33", weight: "0.112" },
          "No.18": { timestamp: "23:52:35", weight: "0.089" },
          "No.19": { timestamp: "23:52:37", weight: "0.100" },
          "No.20": { timestamp: "23:52:39", weight: "0.108" },
          "No.21": { timestamp: "23:52:41", weight: "0.081" },
          "No.22": { timestamp: "23:52:43", weight: "0.094" },
          "No.23": { timestamp: "23:52:45", weight: "0.111" },
          "No.24": { timestamp: "23:52:47", weight: "0.092" },
          "No.25": { timestamp: "23:52:49", weight: "0.080" },
          "No.26": { timestamp: "23:52:51", weight: "0.113" },
          "No.27": { timestamp: "23:52:53", weight: "0.105" },
          "No.28": { timestamp: "23:52:55", weight: "0.093" },
          "No.29": { timestamp: "23:52:57", weight: "0.082" },
          "No.30": { timestamp: "23:52:59", weight: "0.114" },
        },
      },
    },
  },

  // Remarks
  remarks: {
    dataset: {
      "01/02/2024, 12:55:49": {
        issues: "ทดสอบ,เหตุการที่เกิดการเปลี่ยนแปลง",
        cause: "ทดสอบ, สาเหตุ",
        resolve: "ทดสอบ, การแก้ไข",
        notes: "ทดสอบ, หมายเหตุ",
        recorder: "ทดสอบ, ผู้บันทึก",
        role: "Admin",
      },
      "31/03/2024, 02:55:14": {
        issues:
          "น้ำหนักไม่ได้อยู่ในช่วงที่กำหนด \nช่วงที่กำหนด \n(0.970g. - 1.030g.) \nน้ำหนักที่ชั่ง \n['1.006', '2.004'] \nค่าเฉลี่ยที่ได้ 1.505g.",
        cause: "พนักงานลืมกด  re-zero ของเครื่องชั่งในการชั่งน้ำหนักรอบที่2",
        resolve:
          "นำเม็ดยายาชุดเดิมมาชั่งใหม่ในเวลา 03:00 น. ครั้งที่1 \n 0.999 กรัม ครั้งที่2 1.001 g ค่าอยู่ในเกณฑ์การยอมรับผลิตจึงนำไปผลิตต่อ",
        notes: "",
        recorder: "ชิตชนก",
        role: "Superuser",
      },
    },
  },
};

// ข้อมูลบันทึกการปฏิบัติงาน
const dataLog = {
  "07/06/2023, 8:02:29": {
    list: "จบการผลิต",
    details:
      "ชื่อยา: POTRIM                \nเลขที่ผลิต: 30653                \nเครื่องตอก: T11",
    recorder: "สำลี",
    role: "Superuser",
  },
  "07/06/2023, 8:08:57": {
    list: "ตั้งค่าน้ำหนักยา",
    details:
      "ชื่อยา: POTRIM                \nเลขที่ผลิต: 30487R                \nเครื่องตอก: T11",
    recorder: "สำลี",
    role: "Superuser",
  },
  "07/06/2023, 14:10:33": {
    list: "เพิ่ม/แก้ไข ข้อมูลผู้ใช้งาน",
    details:
      "RFID: 3473473470                \nรหัสพนักงาน: 347                \nชื่อ-สกุล: ชัชฎาภรณ์                \nสิทธิการใช้งาน: Superuser",
    recorder: "แอดมิน",
    role: "Superuser",
  },
  "07/06/2023, 17:13:36": {
    list: "เพิ่ม/แก้ไข ข้อมูลผู้ใช้งาน",
    details:
      "RFID: 000000                \nรหัสพนักงาน: 1330                \nชื่อ-สกุล: พิมพ์พร                \nสิทธิการใช้งาน: User",
    recorder: "แอดมิน",
    role: "Superuser",
  },
  "07/06/2023, 19:35:14": {
    list: "ลงบันทึก remarks",
    details:
      'ชื่อยา POTRIM                      \nเลขที่ผลิต 30487R                      \nปัญหาที่พบ: พบเม็ดยาลักษณะ "ผิดปกติ" \nในช่วงเวลาการชั่ง 07/06/2023, 14:26:17                      \nสาเหตุ: พนักงานเลือกข้อความผิด                       \nการแก้ไข: ลักษณะเม็ดยาปกติ                      \nหมายเหตุ: ',
    recorder: "ฉัตรพร",
    role: "Superuser",
  },
  "08/06/2023, 19:06:05": {
    list: "เพิ่ม/แก้ไข ข้อมูลผู้ใช้งาน",
    details:
      "RFID: 1514079705                \nรหัสพนักงาน: 2077                \nชื่อ-สกุล: ณัฐพล                \nสิทธิการใช้งาน: Admin",
    recorder: "แอดมิน",
    role: "Superuser",
  },
  "08/06/2023, 20:27:38": {
    list: "ตั้งค่าน้ำหนักยา",
    details:
      "ชื่อยา: Travan 0.5                \nเลขที่ผลิต: 30201                \nเครื่องตอก: T17",
    recorder: "ฉัตรพร",
    role: "Superuser",
  },
  "09/06/2023, 1:36:17": {
    list: "จบการผลิต",
    details:
      "ระบบเครื่องชั่ง: IPC                \nชื่อยา: POTRIM                \nเลขที่ผลิต: 30487R                \nเครื่องตอก: T11",
    recorder: "ชิตชนก",
    role: "Superuser",
  },
  "09/06/2023, 1:38:27": {
    list: "จบการผลิต",
    details:
      "ระบบเครื่องชั่ง: 10 เม็ด                \nชื่อยา: POTRIM                \nเลขที่ผลิต: 30487R                \nเครื่องตอก: T11",
    recorder: "ชิตชนก",
    role: "Superuser",
  },
  "09/06/2023, 1:43:58": {
    list: "ตั้งค่าน้ำหนักยา",
    details:
      "ชื่อยา: potrim                \nเลขที่ผลิต: 30654                \nเครื่องตอก: T11",
    recorder: "ชิตชนก",
    role: "Superuser",
  },
  "09/06/2023, 13:24:35": {
    list: "ตั้งค่าน้ำหนักยา",
    details:
      "ชื่อยา: travan 0.5                \nเลขที่ผลิต: 30210                \nเครื่องตอก: T17",
    recorder: "สำลี",
    role: "Superuser",
  },
};

const dataSettings = {
  tabletLists: {
    T01: {
      url_ipc:
        "https://docs.google.com/spreadsheets/d/1Z_yI1KQp2YCoDHp8T3Zs5Pw1JMVt3thdrxUnArUv-bo/edit?usp=drive_link",
      url_10s:
        "https://docs.google.com/spreadsheets/d/1XySGAC8aaywquHFKwr_zBBDpOgj99CF15UHe3P3kYF8/edit?usp=drive_link",
    },
  },
  balanceLists: [
    "PI-044",
    "PI-065",
    "PI-066",
    "PI-090",
    "PI-091",
    "PI-123",
    "PI-147",
    "PI-148",
    "PI-149",
    "PI-150",
    "PI-151",
    "PI-152",
    "PI-180",
    "PI-194",
    "PI-195",
    "PI-216",
    "PI-227",
    "PI-228",
    "PI-229",
  ],
  userLists: {
    1514075577: {
      employeeId: "3385",
      usernameTH: "ชิตชนก",
      usernameEN: "Chitchanok",
      role: "Superuser",
    },
    1514079705: {
      employeeId: "2077",
      usernameTH: "ณัฐพล",
      usernameEN: "Nattapon",
      role: "Admin",
    },
    1514088142: {
      employeeId: "3137",
      usernameTH: "ธีรภัทร",
      usernameEN: "Teerapat",
      role: "Admin",
    },
    1514096941: {
      employeeId: "3381",
      usernameTH: "อรทัย",
      usernameEN: "Orathai",
      role: "Superuser",
    },
    1514100775: {
      employeeId: "3365",
      usernameTH: "วันทนีย์",
      usernameEN: "Wantanee",
      role: "Operator",
    },
    1514102360: {
      employeeId: "3384",
      usernameTH: "ประภัสสร",
      usernameEN: "Prapatsorn",
      role: "Operator",
    },
    3473473470: {
      employeeId: "347",
      usernameTH: "ชัชฎาภรณ์",
      usernameEN: "Chatchadaporn",
      role: "Superuser",
    },
    "0006670026": {
      employeeId: "3521",
      usernameTH: "ฉัตรพร",
      usernameEN: "Chatporn",
      role: "Admin",
    },
    "0006600666": {
      employeeId: "3871",
      usernameTH: "สิริยาภรณ์",
      usernameEN: "Siriyaporn",
      role: "Admin",
    },
    "0003781035": {
      employeeId: "3517",
      usernameTH: "สำลี",
      usernameEN: "Samlee",
      role: "Superuser",
    },
    "0006621993": {
      employeeId: "3668",
      usernameTH: "ณัฐกานต์",
      usernameEN: "Natthakarn",
      role: "Operator",
    },
    "0007296392": {
      employeeId: "1111",
      usernameTH: "สำรอง 1",
      usernameEN: "Alternate 1",
      role: "Operator",
    },
    "0006593978": {
      employeeId: "3678",
      usernameTH: "อนุสรณ์",
      usernameEN: "Anusorn",
      role: "Operator",
    },
    "0006662810": {
      employeeId: "3696",
      usernameTH: "กรรณิการ์",
      usernameEN: "Kannika",
      role: "Operator",
    },
    "0006667270": {
      employeeId: "3781",
      usernameTH: "สุนันท์",
      usernameEN: "Sunan",
      role: "Operator",
    },
    "0006663059": {
      employeeId: "3853",
      usernameTH: "เอวลิน",
      usernameEN: "Evelyn",
      role: "Operator",
    },
    "0006676619": {
      employeeId: "3782",
      usernameTH: "สะกุณา",
      usernameEN: "Sakuna",
      role: "Operator",
    },
    "0005186406": {
      employeeId: "3923",
      usernameTH: "อมีนา",
      usernameEN: "Amena",
      role: "Operator",
    },
    "0006677476": {
      employeeId: "3826",
      usernameTH: "สุระกรณ์",
      usernameEN: "Surakorn",
      role: "Operator",
    },
    "0006663152": {
      employeeId: "3872",
      usernameTH: "กัญญาวีย์",
      usernameEN: "Kanyawee",
      role: "Operator",
    },
    "0006669994": {
      employeeId: "3926",
      usernameTH: "ชลิตา",
      usernameEN: "Chalita",
      role: "Operator",
    },
    "0006671160": {
      employeeId: "3927",
      usernameTH: "กาญจนาพร",
      usernameEN: "Kanjanaporn",
      role: "Operator",
    },
    "0006666282": {
      employeeId: "3925",
      usernameTH: "อริษา",
      usernameEN: "Alisa",
      role: "Operator",
    },
    "0006674961": {
      employeeId: "3800",
      usernameTH: "ศศิกาญจน์",
      usernameEN: "Sasikarn",
      role: "Operator",
    },
    "0007293217": {
      employeeId: "4026",
      usernameTH: "สุนิษา",
      usernameEN: "Sunisa ",
      role: "Operator",
    },
    "0007303102": {
      employeeId: "4027",
      usernameTH: "สุภาสินี",
      usernameEN: "Supasinee",
      role: "Operator",
    },
    "0007309121": {
      employeeId: "3926",
      usernameTH: "ชลิตา",
      usernameEN: "Charita",
      role: "Operator",
    },
    "0007293218": {
      employeeId: "5555",
      usernameTH: "สำรอง 5",
      usernameEN: "Alternate 5",
      role: "Operator",
    },
    "000000": {
      employeeId: "1330",
      usernameTH: "พิมพ์พร",
      usernameEN: "Pimporn",
      role: "Inspector",
    },
    "0007275420": {
      employeeId: "3998",
      usernameTH: "วิยะดา",
      usernameEN: "Wiyada",
      role: "Operator",
    },
    "0007273752": {
      employeeId: "3995",
      usernameTH: "ชณายุทธ",
      usernameEN: "Chanayut",
      role: "Operator",
    },
    "0006674800": {
      employeeId: "3939",
      usernameTH: "สโรชา",
      usernameEN: "Sarocha",
      role: "Admin",
    },
    "0007308834": {
      employeeId: "3385",
      usernameTH: "ชิตชนก",
      usernameEN: "Chitchanok ",
      role: "Operator",
    },
    5000000000: {
      employeeId: "2372",
      usernameTH: "พัชรา",
      usernameEN: "Phatchara",
      role: "Inspector",
    },
    5000000001: {
      employeeId: "3662",
      usernameTH: "แก้วมณี",
      usernameEN: "Kaewmanee",
      role: "Inspector",
    },
    5000000002: {
      employeeId: "2538",
      usernameTH: "แพรวนภา",
      usernameEN: "Paewnapra",
      role: "Inspector",
    },
    "000729392": {
      employeeId: "3781",
      usernameTH: "สุนันท์",
      usernameEN: "Sunan",
      role: "Operator",
    },
    "0007296391": {
      employeeId: "3348",
      usernameTH: "ไพลิน",
      usernameEN: "Phailin",
      role: "Operator",
    },
    "0006676620": {
      employeeId: "3782",
      usernameTH: "สะกุณา",
      usernameEN: "Sakuna",
      role: "Operator",
    },
  },
  productLists: {
    "ALPRAZOLAM 0.25": {
      weight_control_10s: {
        meanWeight10s: "1.000",
        percentWeightVariation10s: "2.00%",
        meanWeight10sMin: "3.000",
        meanWeight10sMax: "4.000",
        meanWeightReg10sMin: "5.000",
        meanWeightReg10sMax: "6.000",
        thickness10sMin: "7.00",
        thickness10sMax: "8.00",
      },
      weight_control_ipc: {
        meanWeightIpc: "9.000",
        percentWeightIpc: "10.00%",
        meanWeightAverageIpcMin: "11.000",
        meanWeightAverageIpcMax: "12.000",
        meanWeightVariationIpcMin: "13.000",
        meanWeightVariationIpcMax: "14.000",
        meanWeightRegIpcMin: "15.000",
        meanWeightRegIpcMax: "16.000",
      },
    },
    "ALPRAZOLAM 0.5": {
      weight_control_10s: {
        meanWeight10s: "",
        percentWeightVariation10s: "",
        meanWeight10sMin: "",
        meanWeight10sMax: "",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "",
        percentWeightIpc: "",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    "AMARAX 2": {
      weight_control_10s: {
        meanWeight10s: "",
        percentWeightVariation10s: "",
        meanWeight10sMin: "",
        meanWeight10sMax: "",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "",
        percentWeightIpc: "",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    AMCO: {
      weight_control_10s: {
        meanWeight10s: "9.000",
        percentWeightVariation10s: "2.00%",
        meanWeight10sMin: "8.820",
        meanWeight10sMax: "9.180",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "0.900",
        percentWeightIpc: "4.00%",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    "AMLOVASC 5": {
      weight_control_10s: {
        meanWeight10s: "1.910",
        percentWeightVariation10s: "3.00%",
        meanWeight10sMin: "1.860",
        meanWeight10sMax: "1.960",
        meanWeightReg10sMin: "1.760",
        meanWeightReg10sMax: "2.040",
        thickness10sMin: "2.90",
        thickness10sMax: "3.40",
      },
      weight_control_ipc: {
        meanWeightIpc: "0.191",
        percentWeightIpc: "6.00%",
        meanWeightAverageIpcMin: "0.186",
        meanWeightAverageIpcMax: "0.196",
        meanWeightVariationIpcMin: "0.180",
        meanWeightVariationIpcMax: "0.202",
        meanWeightRegIpcMin: "0.177",
        meanWeightRegIpcMax: "0.205",
      },
    },
    ANTAFIT: {
      weight_control_10s: {
        meanWeight10s: "",
        percentWeightVariation10s: "",
        meanWeight10sMin: "",
        meanWeight10sMax: "",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "",
        percentWeightIpc: "",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    "APURINOL 300": {
      weight_control_10s: {
        meanWeight10s: "5.500",
        percentWeightVariation10s: "2.00%",
        meanWeight10sMin: "5.390",
        meanWeight10sMax: "5.610",
        meanWeightReg10sMin: "5.230",
        meanWeightReg10sMax: "5.770",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "0.550",
        percentWeightIpc: "4.00%",
        meanWeightAverageIpcMin: "0.539",
        meanWeightAverageIpcMax: "0.561",
        meanWeightVariationIpcMin: "0.528",
        meanWeightVariationIpcMax: "0.572",
        meanWeightRegIpcMin: "0.523",
        meanWeightRegIpcMax: "0.577",
      },
    },
    "ASCOT 300": {
      weight_control_10s: {
        meanWeight10s: "",
        percentWeightVariation10s: "",
        meanWeight10sMin: "",
        meanWeight10sMax: "",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "",
        percentWeightIpc: "",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    "ASCOT 81": {
      weight_control_10s: {
        meanWeight10s: "0.980",
        percentWeightVariation10s: "3.00%",
        meanWeight10sMin: "0.890",
        meanWeight10sMax: "1.070",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "0.098",
        percentWeightIpc: "8.00%",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    ASMALINE: {
      weight_control_10s: {
        meanWeight10s: "",
        percentWeightVariation10s: "",
        meanWeight10sMin: "",
        meanWeight10sMax: "",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "",
        percentWeightIpc: "",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    BENCLAMIN: {
      weight_control_10s: {
        meanWeight10s: "",
        percentWeightVariation10s: "",
        meanWeight10sMin: "",
        meanWeight10sMax: "",
        meanWeightReg10sMin: "",
        meanWeightReg10sMax: "",
        thickness10sMin: "",
        thickness10sMax: "",
      },
      weight_control_ipc: {
        meanWeightIpc: "",
        percentWeightIpc: "",
        meanWeightAverageIpcMin: "",
        meanWeightAverageIpcMax: "",
        meanWeightVariationIpcMin: "",
        meanWeightVariationIpcMax: "",
        meanWeightRegIpcMin: "",
        meanWeightRegIpcMax: "",
      },
    },
    BERCLOMIN: {
      weight_control_10s: {
        meanWeight10s: "6.700",
        percentWeightVariation10s: "2.00%",
        meanWeight10sMin: "6.570",
        meanWeight10sMax: "6.830",
        meanWeightReg10sMin: "6.270",
        meanWeightReg10sMax: "6.930",
        thickness10sMin: "5.30",
        thickness10sMax: "5.80",
      },
      weight_control_ipc: {
        meanWeightIpc: "0.670",
        percentWeightIpc: "4.00%",
        meanWeightAverageIpcMin: "0.657",
        meanWeightAverageIpcMax: "0.683",
        meanWeightVariationIpcMin: "0.644",
        meanWeightVariationIpcMax: "0.696",
        meanWeightRegIpcMin: "0.637",
        meanWeightRegIpcMax: "0.703",
      },
    },
  },
};

const productionLists = {
  sheetLists10s: {
    "เครื่องตอก T02 (LOT. ปัจจุบัน)":
      "https://docs.google.com/spreadsheets/d/1XySGAC8aaywquHFKwr_zBBDpOgj99CF15UHe3P3kYF8/edit?usp=drive_link",
    "เครื่องตอก T01 (LOT. ปัจจุบัน)":
      "https://docs.google.com/spreadsheets/d/1XySGAC8aaywquHFKwr_zBBDpOgj99CF15UHe3P3kYF8/edit?usp=drive_link",
  },
  sheetListsIPC: {
    "เครื่องตอก T02 (LOT. ปัจจุบัน)":
      "https://docs.google.com/spreadsheets/d/1Z_yI1KQp2YCoDHp8T3Zs5Pw1JMVt3thdrxUnArUv-bo/edit?usp=drive_link",
    "เครื่องตอก T01 (LOT. ปัจจุบัน)":
      "https://docs.google.com/spreadsheets/d/1Z_yI1KQp2YCoDHp8T3Zs5Pw1JMVt3thdrxUnArUv-bo/edit?usp=drive_link",
  },
};

const weightsTest = [
  {
    timestamp: "01/02/2024, 12:35:43",
    type: "ONLINE",
    weight1: "0.982",
    weight2: "0.981",
    characteristics: "ปกติ",
    operator: "กัญญาวีย์",
    inspector: "-",
    thickness: [
      "2.81",
      "2.84",
      "2.79",
      "2.81",
      "2.84",
      "2.83",
      "2.79",
      "2.80",
      "2.85",
      "2.81",
    ],
  },
  {
    timestamp: "01/02/2024, 12:55:49",
    type: "ONLINE",
    weight1: "0.980",
    weight2: "0.978",
    characteristics: "ปกติ",
    operator: "กัญญาวีย์",
    inspector: "อรทัย",
    thickness: ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
  },
  {
    timestamp: "01/02/2024, 14:56:08",
    type: "ONLINE",
    weight1: "0.985",
    weight2: "0.978",
    characteristics: "ปกติ",
    operator: "กัญญาวีย์",
    inspector: "อรทัย",
    thickness: [
      "2.77",
      "2.80",
      "2.77",
      "2.78",
      "2.79",
      "2.77",
      "2.75",
      "2.75",
      "2.78",
      "2.79",
    ],
  },
];


weightsTest.forEach(function(data) {
  console.log(data)
});