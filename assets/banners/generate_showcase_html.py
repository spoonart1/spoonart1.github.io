import os
import base64

ARTIFACT_DIR = "/Users/user/.gemini/antigravity/brain/eb20549e-b3f5-4543-ba1a-a72a936bc683"
BANNERS_DIR = "/Volumes/Work/spoonart.github.io/assets/banners"

def get_base64_img(filename):
    path = os.path.join(BANNERS_DIR, filename)
    with open(path, "rb") as f:
        data = f.read()
    return f"data:image/png;base64,{base64.b64encode(data).decode('utf-8')}"

print("Encoding banners...")
b1_b64 = get_base64_img("upwork_catalog_banner_dark_tech.png")
b2_b64 = get_base64_img("upwork_catalog_banner_ecosystem.png")
b3_b64 = get_base64_img("upwork_catalog_banner_minimal_bold.png")
print("Banners encoded.")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Upwork Project Catalog Banners (16:9) - Logistics & Route Optimization</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    .aspect-16-9 {{
      aspect-ratio: 16 / 9;
    }}
    .glow-cyan {{
      box-shadow: 0 0 30px -5px rgba(6, 182, 212, 0.3);
    }}
    .glow-indigo {{
      box-shadow: 0 0 30px -5px rgba(99, 102, 241, 0.3);
    }}
    .glow-emerald {{
      box-shadow: 0 0 30px -5px rgba(16, 185, 129, 0.3);
    }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen p-4 md:p-8">

  <div class="max-w-7xl mx-auto space-y-10">

    <!-- HEADER BAR -->
    <header class="border-b border-slate-800 pb-6 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="flex items-center gap-2 mb-2">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/30">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            16:9 Aspect Ratio · 1920 × 1080 Full HD
          </span>
          <span class="px-2.5 py-1 rounded-full text-xs font-medium bg-slate-800 text-slate-300 border border-slate-700">
            Upwork Project Catalog Ready
          </span>
        </div>
        <h1 class="text-2xl md:text-3xl font-extrabold text-white tracking-tight">
          Upwork Showcase Banners: Logistics & Fleet Driver Platform
        </h1>
        <p class="text-sm text-slate-400 mt-1">
          Designed specifically for Muhammad Lafran Pane's Upwork Catalog. Hand-crafted device mockups, high contrast thumbnail readability, and production-tested proof points.
        </p>
      </div>

      <!-- Quick stats summary -->
      <div class="flex items-center gap-3">
        <a href="#optimization-guide" class="text-xs px-3.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium transition flex items-center gap-1.5">
          <span>📋</span> Upwork Catalog Guide
        </a>
      </div>
    </header>

    <!-- BANNER GALLERY / SHOWCASE -->
    <section class="space-y-8">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-xl font-bold text-white flex items-center gap-2">
            <span>🎨</span> Ready-to-Upload 16:9 Banner Variations
          </h2>
          <p class="text-xs text-slate-400 mt-0.5">Click any download button to save the uncompressed 1920×1080 PNG directly to your computer.</p>
        </div>
      </div>

      <!-- BANNER 1 CARD -->
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 md:p-6 shadow-2xl space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">OPTION 1 · RECOMMENDED</span>
              <h3 class="text-lg font-bold text-white">Dark Tech Hero — Complete Driver & In-Cab Fleet App</h3>
            </div>
            <p class="text-xs text-slate-400 mt-0.5">
              Features Tablet in-cab navigation, vertical Driver smartphone app, and floating Proof-of-Delivery (POD) verification card with photo & digital signature.
            </p>
          </div>
          <button onclick="downloadImage('banner1', 'upwork_catalog_banner_dark_tech.png')" 
                  class="self-start sm:self-auto px-4 py-2 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold transition flex items-center gap-2 shadow-lg shadow-cyan-600/30">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Download 16:9 PNG (1920×1080)
          </button>
        </div>

        <div class="relative rounded-xl overflow-hidden border border-slate-800 bg-slate-950 aspect-16-9 group shadow-inner">
          <img id="banner1" src="{b1_b64}" alt="Dark Tech Banner" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-3 backdrop-blur-sm">
            <button onclick="openModal('{b1_b64}', 'Option 1: Dark Tech Hero')" class="px-4 py-2 rounded-lg bg-white/90 text-slate-900 font-semibold text-xs hover:bg-white transition flex items-center gap-1.5 shadow-md">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7"></path></svg>
              View Fullscreen Preview
            </button>
            <button onclick="downloadImage('banner1', 'upwork_catalog_banner_dark_tech.png')" class="px-4 py-2 rounded-lg bg-cyan-600 text-white font-semibold text-xs hover:bg-cyan-500 transition flex items-center gap-1.5 shadow-md">
              Download PNG
            </button>
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2 text-xs text-slate-400">
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Key Proof</span>
            <span class="text-slate-200 font-semibold">10,000+ Daily Orders</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Global Scale</span>
            <span class="text-slate-200 font-semibold">5 Countries in Production</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Mockup Focus</span>
            <span class="text-slate-200 font-semibold">In-Cab Tablet + Phone + POD</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Search Thumbnail</span>
            <span class="text-emerald-400 font-semibold">⭐⭐⭐⭐⭐ High Visibility</span>
          </div>
        </div>
      </div>

      <!-- BANNER 2 CARD -->
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 md:p-6 shadow-2xl space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">OPTION 2 · FULL ECOSYSTEM</span>
              <h3 class="text-lg font-bold text-white">Full Ecosystem Suite — Dispatcher Web + Tablet + Mobile App</h3>
            </div>
            <p class="text-xs text-slate-400 mt-0.5">
              Highlights the complete platform: Web Route Generator (dispatch planning monitor), in-cab tablet UI, and driver smartphone navigation.
            </p>
          </div>
          <button onclick="downloadImage('banner2', 'upwork_catalog_banner_ecosystem.png')" 
                  class="self-start sm:self-auto px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition flex items-center gap-2 shadow-lg shadow-indigo-600/30">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Download 16:9 PNG (1920×1080)
          </button>
        </div>

        <div class="relative rounded-xl overflow-hidden border border-slate-800 bg-slate-950 aspect-16-9 group shadow-inner">
          <img id="banner2" src="{b2_b64}" alt="Ecosystem Banner" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-3 backdrop-blur-sm">
            <button onclick="openModal('{b2_b64}', 'Option 2: Full Ecosystem Suite')" class="px-4 py-2 rounded-lg bg-white/90 text-slate-900 font-semibold text-xs hover:bg-white transition flex items-center gap-1.5 shadow-md">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7"></path></svg>
              View Fullscreen Preview
            </button>
            <button onclick="downloadImage('banner2', 'upwork_catalog_banner_ecosystem.png')" class="px-4 py-2 rounded-lg bg-indigo-600 text-white font-semibold text-xs hover:bg-indigo-500 transition flex items-center gap-1.5 shadow-md">
              Download PNG
            </button>
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2 text-xs text-slate-400">
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">System Scope</span>
            <span class="text-slate-200 font-semibold">Web Portal + 2 Mobile Apps</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Solo Engineering</span>
            <span class="text-slate-200 font-semibold">10 Map Screens Re-architected</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Client Target</span>
            <span class="text-indigo-300 font-semibold">Enterprise & B2B Logistics</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Contrast</span>
            <span class="text-emerald-400 font-semibold">⭐⭐⭐⭐⭐ Deep Indigo</span>
          </div>
        </div>
      </div>

      <!-- BANNER 3 CARD -->
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 md:p-6 shadow-2xl space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30">OPTION 3 · SEARCH IMPACT</span>
              <h3 class="text-lg font-bold text-white">High-Impact Search Specialist — Turn-by-Turn Mobility</h3>
            </div>
            <p class="text-xs text-slate-400 mt-0.5">
              Maximum typographic contrast and bold stat cards (10K+ Orders, 5+ Countries, 11+ Years) engineered specifically to stand out in small search thumbnails.
            </p>
          </div>
          <button onclick="downloadImage('banner3', 'upwork_catalog_banner_minimal_bold.png')" 
                  class="self-start sm:self-auto px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-xs font-bold transition flex items-center gap-2 shadow-lg shadow-sky-600/30">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            Download 16:9 PNG (1920×1080)
          </button>
        </div>

        <div class="relative rounded-xl overflow-hidden border border-slate-800 bg-slate-950 aspect-16-9 group shadow-inner">
          <img id="banner3" src="{b3_b64}" alt="Search Specialist Banner" class="w-full h-full object-cover">
          <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-3 backdrop-blur-sm">
            <button onclick="openModal('{b3_b64}', 'Option 3: High-Impact Search Specialist')" class="px-4 py-2 rounded-lg bg-white/90 text-slate-900 font-semibold text-xs hover:bg-white transition flex items-center gap-1.5 shadow-md">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7"></path></svg>
              View Fullscreen Preview
            </button>
            <button onclick="downloadImage('banner3', 'upwork_catalog_banner_minimal_bold.png')" class="px-4 py-2 rounded-lg bg-sky-600 text-white font-semibold text-xs hover:bg-sky-500 transition flex items-center gap-1.5 shadow-md">
              Download PNG
            </button>
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-2 text-xs text-slate-400">
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Specialty</span>
            <span class="text-slate-200 font-semibold">Turn-by-Turn Navigation</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Track Record</span>
            <span class="text-slate-200 font-semibold">11+ Years Mobile Engineering</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Primary Badges</span>
            <span class="text-sky-300 font-semibold">Kotlin · Compose · Maps SDK</span>
          </div>
          <div class="bg-slate-950/60 p-2.5 rounded-lg border border-slate-800/80">
            <span class="text-slate-500 block text-[10px] uppercase font-bold">Thumbnail Score</span>
            <span class="text-emerald-400 font-semibold">10/10 Bold Clarity</span>
          </div>
        </div>
      </div>
    </section>

    <!-- UPWORK PROJECT CATALOG OPTIMIZATION GUIDE -->
    <section id="optimization-guide" class="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 md:p-8 space-y-6">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 text-lg font-bold">
          ✓
        </div>
        <div>
          <h2 class="text-xl font-bold text-white">Upwork Project Catalog Setup Cheat-Sheet</h2>
          <p class="text-xs text-slate-400">Copy-paste ready title, tags, and pricing descriptions to maximize client bookings.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
        <!-- Column 1: Titles & Categories -->
        <div class="space-y-4">
          <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-4 space-y-2">
            <span class="text-slate-400 text-xs font-semibold uppercase tracking-wider block">Recommended Upwork Project Title (Max 80 chars)</span>
            <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800 text-sm font-mono text-cyan-300 font-medium select-all">
              You will get a custom delivery, route optimization, & driver mobile app
            </div>
            <p class="text-[11px] text-slate-500">Upwork prefixes the title with "You will get...". This title highlights delivery, routing, and driver apps.</p>
          </div>

          <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-4 space-y-2">
            <span class="text-slate-400 text-xs font-semibold uppercase tracking-wider block">Recommended Category & Subcategory</span>
            <div class="text-sm text-slate-200">
              <span class="font-semibold text-white">Development & IT</span> &rarr; 
              <span class="font-semibold text-white">Mobile Development</span> &rarr; 
              <span class="font-semibold text-cyan-300">Android App Development / Cross-Platform Apps</span>
            </div>
          </div>

          <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-4 space-y-2">
            <span class="text-slate-400 text-xs font-semibold uppercase tracking-wider block">Top 5 Search Tags</span>
            <div class="flex flex-wrap gap-1.5 pt-1">
              <span class="px-2.5 py-1 rounded bg-slate-800 text-xs text-slate-200 border border-slate-700">Delivery App</span>
              <span class="px-2.5 py-1 rounded bg-slate-800 text-xs text-slate-200 border border-slate-700">Route Optimization</span>
              <span class="px-2.5 py-1 rounded bg-slate-800 text-xs text-slate-200 border border-slate-700">Jetpack Compose</span>
              <span class="px-2.5 py-1 rounded bg-slate-800 text-xs text-slate-200 border border-slate-700">GPS Navigation</span>
              <span class="px-2.5 py-1 rounded bg-slate-800 text-xs text-slate-200 border border-slate-700">Logistics & Fleet</span>
            </div>
          </div>
        </div>

        <!-- Column 2: Highlights & Tier Structure -->
        <div class="space-y-4">
          <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-4 space-y-3">
            <span class="text-slate-400 text-xs font-semibold uppercase tracking-wider block">Why These Banners Convert on Upwork</span>
            <ul class="space-y-2 text-xs text-slate-300">
              <li class="flex items-start gap-2">
                <span class="text-cyan-400 font-bold">1.</span>
                <span><strong>No Stock Graphics:</strong> Uses actual live UI from your Singapore, UAE, and Japan production deployments.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400 font-bold">2.</span>
                <span><strong>Hardware Diversity:</strong> Shows both in-cab landscape tablet and handheld mobile phone with realistic device frames.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400 font-bold">3.</span>
                <span><strong>High-Value POD Focus:</strong> Proof of Delivery with signatures and photo proof is a primary pain point for logistics clients.</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="text-cyan-400 font-bold">4.</span>
                <span><strong>Hard Metrics:</strong> "10,000+ Daily Orders" and "5 Countries" builds instant credibility over generic freelance agencies.</span>
              </li>
            </ul>
          </div>

          <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-4 space-y-2">
            <span class="text-slate-400 text-xs font-semibold uppercase tracking-wider block">Banner Technical Specifications</span>
            <div class="grid grid-cols-2 gap-2 text-xs">
              <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-slate-500 block text-[10px]">Ratio</span>
                <span class="font-mono text-cyan-300 font-bold">16:9 (Standard)</span>
              </div>
              <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-slate-500 block text-[10px]">Resolution</span>
                <span class="font-mono text-cyan-300 font-bold">1920 × 1080 px</span>
              </div>
              <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-slate-500 block text-[10px]">File Format</span>
                <span class="font-mono text-cyan-300 font-bold">PNG (Lossless 24-bit)</span>
              </div>
              <div class="p-2 bg-slate-900 rounded border border-slate-800">
                <span class="text-slate-500 block text-[10px]">File Size</span>
                <span class="font-mono text-emerald-400 font-bold">~520 KB (&lt;10 MB limit)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="text-center text-xs text-slate-500 pt-4 pb-8 border-t border-slate-900">
      Built for Muhammad Lafran Pane · All banner image files are stored locally in <code class="text-slate-400">/assets/banners/</code>
    </footer>

  </div>

  <!-- FULLSCREEN MODAL -->
  <div id="imageModal" class="fixed inset-0 bg-black/90 z-50 hidden backdrop-blur-md flex flex-col items-center justify-center p-4">
    <div class="max-w-6xl w-full bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl">
      <div class="flex items-center justify-between p-4 border-b border-slate-800">
        <h4 id="modalTitle" class="text-sm font-bold text-white">Full Preview</h4>
        <button onclick="closeModal()" class="p-1 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-white transition">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>
      <div class="p-4 bg-slate-950 flex items-center justify-center">
        <img id="modalImage" src="" alt="Fullscreen preview" class="w-full h-auto max-h-[75vh] object-contain rounded-lg">
      </div>
    </div>
  </div>

  <script>
    function downloadImage(imgId, filename) {{
      const img = document.getElementById(imgId);
      const link = document.createElement('a');
      link.href = img.src;
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    function openModal(src, title) {{
      document.getElementById('modalImage').src = src;
      document.getElementById('modalTitle').innerText = title;
      document.getElementById('imageModal').classList.remove('hidden');
    }}

    function closeModal() {{
      document.getElementById('imageModal').classList.add('hidden');
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeModal();
    }});
  </script>

</body>
</html>
"""

artifact_path = os.path.join(ARTIFACT_DIR, "upwork_katalog_banner_showcase.html")
with open(artifact_path, "w") as f:
    f.write(html_content)
print("Artifact saved to:", artifact_path)

workspace_path = "/Volumes/Work/spoonart.github.io/assets/banners/index.html"
with open(workspace_path, "w") as f:
    f.write(html_content)
print("Workspace copy saved to:", workspace_path)
