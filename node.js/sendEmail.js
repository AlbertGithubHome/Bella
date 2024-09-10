const nodemailer = require('nodemailer');

// 创建一个 SMTP 客户端配置
let transporter = nodemailer.createTransport({
  service: 'hotmail',
  auth: {
    user: 'ai.2338@hotmail.com', // 替换为你的 Hotmail 地址
    pass: 'ai2338'               // 替换为你的 Hotmail 密码
  }
});

// 邮件选项
let mailOptions = {
  from: 'ai.2338@hotmail.com',   // 替换为你的 Hotmail 地址
  to: 'shihengzhen101@163.com',  // 替换为收件人的电子邮件地址
  subject: 'Hello from Node.js',
  text: 'This is a test email sent from a Node.js application!'
};

// 发送邮件
transporter.sendMail(mailOptions, function(error, info) {
  if (error) {
    return console.log(error);
  }
  console.log('Email sent: ' + info.response);
});
