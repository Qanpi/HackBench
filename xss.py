import asyncio
from pyppeteer import launch

URL = 'https://example.com'  # Replace with the target URL

async def test_pyppeteer():
    """
    Test script that opens a page using pyppeteer browser automation.
    """
    browser = None
    try:
        # Launch browser with additional arguments for better compatibility
        browser = await launch(
            headless=False,  # Set to False to see the browser window
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--disable-extensions',
                '--disable-background-timer-throttling',
                '--disable-backgrounding-occluded-windows',
                '--disable-renderer-backgrounding',
                '--no-first-run',
                '--no-default-browser-check'
            ],
            executablePath=None,  # Let pyppeteer find Chromium
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False
        )
        
        # Create a new page
        page = await browser.newPage()
        
        # Set a user agent to avoid detection
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        # Set viewport
        await page.setViewport({'width': 1280, 'height': 720})
        
        # Navigate to the URL with timeout
        print(f"Navigating to {URL}...")
        await page.goto(URL, {'waitUntil': 'networkidle0', 'timeout': 30000})
        
        # Get page title
        title = await page.title()
        print(f"Page title: {title}")
        
        # Get page content
        content = await page.content()
        print(f"Page content length: {len(content)} characters")
        
        # Get page URL (in case of redirects)
        current_url = page.url
        print(f"Current URL: {current_url}")
        
        # Take a screenshot (optional)
        # await page.screenshot({'path': 'test_screenshot.png', 'fullPage': True})
        # print("Screenshot saved as test_screenshot.png")
        
        return True
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    
    finally:
        # Ensure browser is closed properly
        if browser:
            try:
                # await browser.close()
                print("Browser closed successfully")
            except Exception as e:
                print(f"Error closing browser: {e}")

# Run the test
result = asyncio.run(test_pyppeteer())
print(f"Test result: {result}")