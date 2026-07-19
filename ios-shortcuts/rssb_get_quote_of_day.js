let wv = new WebView();
await wv.loadURL("https://rssb.org/quotes.html");

let quoteData = await wv.evaluateJavaScript(`
  (function(){
    return {
      quote: document.getElementById("quote").innerText,
      author: document.getElementById("author").innerText
    };
  })();
`);

stringfied =JSON.stringify(quoteData);

Script.setShortcutOutput(stringfied);
Script.complete();
