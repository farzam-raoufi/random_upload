module.exports = {
  apps : [{
    name: "uploader",
    script: "./random_upload.py",
    env: {
      URLS: "https://www.amazon.com/,https://www.wikipedia.org/,https://www.digikala.com/,https://us.yahoo.com/",
    },
    env_production: {
      URLS: "https://www.amazon.com/,https://www.wikipedia.org/,https://www.digikala.com/,https://us.yahoo.com/",
    }
  }]
}