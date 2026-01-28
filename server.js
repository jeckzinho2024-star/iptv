import express from "express";
import fetch from "node-fetch";

const app = express();

const M3U_URL = "http://gcorecdns.xyz:80/get.php?username=110453920&password=467071310&type=m3u_plus&output=mpegts";

app.get("/m3u", async (req, res) => {
  try {
    const r = await fetch(M3U_URL);
    const text = await r.text();

    res.setHeader("Access-Control-Allow-Origin", "*");
    res.send(text);
  } catch (e) {
    res.status(500).send("Erro ao carregar M3U");
  }
});

app.listen(process.env.PORT || 3000);
