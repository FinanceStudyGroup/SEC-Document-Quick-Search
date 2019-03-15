# SEC Document Quick Search Locator
This is a document locator for searching SEC EDGAR.

-----------------------------------------------------------------------------------------------------------------
Within finance, much of the work of analyzing corporate performance and the value drivers behind share price
begins with a financial model. These models consist of Excel files of dynamically linked documents that
describe and predict historical and future performance of a given company, using its accounting.

We can use the framework of financial accounting to analyze the performance of companies and predict the likely
future cash flows to these businesses. However, this all begins with the documents.

To facilitate this process, we've built the following SEC document locator for quick document searches,
right from the command line.

-----------------------------------------------------------------------------------------------------------------


To run this program, be sure to get [Selenium](https://www.seleniumhq.org/), and the most recent releases of [Google Chrome](https://www.google.com/chrome/?brand=CHBF&utm_source=bing&utm_medium=cpc&utm_campaign=1005992%20%7C%20Chrome%20Win10%20%7C%20DR%20%7C%20ESS01%20%7C%20NA%20%7C%20US%20%7C%20en%20%7C%20Desk%20%7C%20BING%20SEM%20%7C%20BKWS%20~%20Top%20KWDS%20-%20Exact&utm_term=google%20chrome&utm_content=Google%20Chrome%20-%20Exact&ds_kid=43700010220923516&gclid=CNupzfPj--ACFduGxQIdWPcHaA&gclsrc=ds),
and [Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=2.46/).

The Selenium package for Python allows for automation of an instance of the web browser.

Specifically, we can write Python code to use the Selenium package to run Chrome Driver and control Google Chrome.

In this way, we can automate tedious processes of populating address bars, clicking buttons, and constantly
repeating the same workflows.

From the command line, we can simply run,

```
python SEC.py
```
after which, we will be prompted for a ticker symbol and document -- as an example we might run,

Ticker:
```
EMN
```

Document:
```
10-K
```

whereby, with relative ease we can quickly navigate to SEC EDGAR's search results for all of Eastman Chemical Company's
most recent annual reports.

Similarly, we could do this for the Forms 10-Q or 20-F, as the case may be. The SEC Document Locator allows for quick
access to any SEC-filed materials available through EDGAR.
