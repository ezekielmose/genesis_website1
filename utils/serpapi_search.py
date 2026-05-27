import requests

# ======================================
# SERPAPI CONFIG
# ======================================
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"

# NOTE: replace with your real API key or load from env
SERPAPI_API_KEY = "YOUR_SERPAPI_API_KEY"

# ======================================
# SEARCH FUNCTION
# ======================================
def search_instagram_profile(query: str):
    """
    Searches Google via SerpAPI and returns first Instagram link found.
    """

    instagram_link = None

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }

    try:
        response = requests.get(SERPAPI_ENDPOINT, params=params, timeout=20)
        data = response.json()

        for result in data.get("organic_results", []):
            link = result.get("link", "")

            if "instagram.com" in link:
                instagram_link = link
                break

        return instagram_link, data

    except Exception as e:
        return None, {"error": str(e)}
