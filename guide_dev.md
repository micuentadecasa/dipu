# Developer guide

## 1. Run locally on your computer

From the project root:

```bash
cd frontend
npm install
npm run dev
```

Open the URL shown by Vite, normally:

```text
http://localhost:5173
```

This version is static, so you do **not** need to run `app.py`, Flask, SQLite, or Python.

## 2. Test the production build locally

This is closer to what GitHub Pages will serve:

```bash
cd frontend
npm run build
npm run preview
```

Open the preview URL, normally:

```text
http://localhost:4173
```

## 3. See the app from your mobile while developing

Your computer and mobile must be connected to the same Wi-Fi.

### Step A: start Vite exposing it to the local network

```bash
cd frontend
npm run dev -- --host 0.0.0.0
```

Vite will show something similar to:

```text
Local:   http://localhost:5173/
Network: http://192.168.1.50:5173/
```

### Step B: open the Network URL on your phone

On the mobile browser, open the `Network` URL, for example:

```text
http://192.168.1.50:5173/
```

If Vite does not show the network URL, get your Mac IP with:

```bash
ipconfig getifaddr en0
```

Then open:

```text
http://YOUR_MAC_IP:5173/
```

Example:

```text
http://192.168.1.50:5173/
```

### If it does not load on mobile

Check:

1. Computer and phone are on the same Wi-Fi.
2. You started Vite with `--host 0.0.0.0`.
3. macOS firewall is not blocking Node/Vite.
4. You are using `http://`, not `https://`.
5. The port is correct, usually `5173`.

## 4. Push to GitHub

If this is a new repository:

```bash
git init
git add .
git commit -m "Static exam app for GitHub Pages"
git branch -M main
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin main
```

If the repository already exists:

```bash
git add .
git commit -m "Improve mobile app and expand question bank"
git push
```

## 5. Enable GitHub Pages

The project already includes this workflow:

```text
.github/workflows/deploy.yml
```

To enable publishing:

1. Go to the GitHub repository.
2. Open **Settings**.
3. Open **Pages**.
4. In **Build and deployment**, choose:

```text
Source: GitHub Actions
```

5. Push to `main`.
6. Go to the **Actions** tab and wait for the deploy workflow to finish.

The site will be available at:

```text
https://YOUR_USER.github.io/YOUR_REPO/
```

## 6. Check the GitHub Pages version from mobile

After deployment finishes:

1. Open the GitHub Pages URL on your phone.
2. Add it to your home screen if you want app-like access:
   - iPhone Safari: Share button → **Add to Home Screen**.
   - Android Chrome: menu `⋮` → **Add to Home screen**.

## 7. Question bank

The source question file is:

```text
seed_data.py
```

The static GitHub Pages question file is:

```text
frontend/src/questions.js
```

After changing `seed_data.py`, regenerate the static question bank with:

```bash
python3 - <<'PY'
import json
from seed_data import SEED_QUESTIONS
qs = []
for i, q in enumerate(SEED_QUESTIONS, 1):
    qs.append({'id': i, **q})
with open('frontend/src/questions.js', 'w', encoding='utf-8') as f:
    f.write('// Generated from seed_data.py. Static question bank for GitHub Pages.\n')
    f.write('export const QUESTIONS = ')
    f.write(json.dumps(qs, ensure_ascii=False, indent=2))
    f.write('\n')
print(f'Generated {len(qs)} questions')
PY
```

Then test:

```bash
cd frontend
npm run build
```
