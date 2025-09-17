---

## What It Does

- Authenticates with Spotify via environment variables (Spotify Client ID / Secret, etc.).
- Fetches data from Spotify (e.g. playlist contents, saved tracks).
- Writes a text file containing the fetched data.  
- A second script (`downloader.py`) processes or uses that text file for further actions.  

---

- Setup

   ```bash
   git clone https://github.com/ryan-mangeno/Spotify-API.git
   cd Spotify-API
   python3 -m venv .env
   source .env/bin/activate
   pip install -r requirements.txt

   ```
- Env Variables:
  You will need to set you vars based on your spotify developer account available (here)[https://developer.spotify.com/documentation/web-api/tutorials/getting-started]
  ```
  SPOTIFY_SECRET
  SPOTIFY_CLIENT_ID
  ```
