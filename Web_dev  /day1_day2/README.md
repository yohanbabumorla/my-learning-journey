# 🌐 Web Development — Day 1 & Day 2

## 🧠 Topics Covered

### 🗓️ Day 1 — HTML Basics + Simple CSS
- HTML Elements: `<button>`, `<p>`, `<a>`
- Attributes: `href`, `target`
- Linking to internal & external pages
- Basic CSS button styling (colors, borders, background)

### 🗓️ Day 2 — CSS Transitions + Hover + Shadows
- Button customization (border-radius, width, color)
- Hover & active states
- Opacity & transition effects
- Box shadows for modern UI buttons

---

## 🧩 Practice Snippets

### 🔹 Day 1 — Basic Buttons and Links
```html
<button>Yohan</button>
<button>Fruits</button>

<p>Hello, World!</p>
<p>Hello, World! Today I do some exercises</p>

<a href="https://www.google.com/">Search with Google</a>
<a href="https://www.google.com/" target="_blank">Search with Google (new tab)</a>
<a href="C:\Users\JARVIS\OneDrive\Desktop\full stack\HTML\Lesson 1\1c.html">Another Site</a>

<a href="https://www.amazon.com/">Back to Amazon</a>
<p>Nike Black Running Shoes</p>
<p>$39 – in stock.</p>
<p>Free delivery tomorrow.</p>
<button>Add to Cart</button>
<button>Buy Now</button>

🔹 Day 2 — Button Hover & Transition Effects
<style>
  .Request-button {
    background-color: black;
    color: white;
    cursor: pointer;
    height: 40px;
    width: 120px;
    font-size: 13px;
    transition: opacity 0.15s;
    margin-right: 8px;
    border-style: solid;
    margin-bottom: 10px;
  }
  .Request-button:hover { opacity: 0.7; }
  .Request-button:active { opacity: 0.5; }

  .Addtocart-button {
    height: 40px;
    width: 200px;
    border-radius: 100px;
    background-color: rgb(240,197,43);
    border-color: rgb(209,154,0);
    border-style: solid;
    cursor: pointer;
    font-weight: bold;
    margin-right: 10px;
    margin-bottom: 10px;
  }
  .Addtocart-button:hover { background-color: rgb(248,187,2); }

  .signup-button {
    height: 40px;
    width: 100px;
    border-radius: 8px;
    cursor: pointer;
    background-color: green;
    border: none;
    color: white;
    font-weight: bold;
    font-size: 14px;
    transition: box-shadow 0.15s;
    margin-right: 10px;
    margin-bottom: 10px;
  }
  .signup-button:hover { box-shadow: 0 5px 10px rgba(0,0,0,0.5); }

  .getstarted-button {
    height: 40px;
    width: 120px;
    background-color: rgb(139,17,253);
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.15s;
    margin-bottom: 10px;
    margin-right: 10px;
  }
  .getstarted-button:hover { background-color: rgb(86,2,164); }

  .Download-button {
    height: 30px;
    width: 100px;
    font-size: 11px;
    cursor: pointer;
    background-color: white;
    color: rgb(44,43,43);
    border-radius: 4px;
    border-style: solid;
    border-color: rgb(44,43,43);
    transition: color 0.15s, background-color 0.15s;
    margin-right: 10px;
    margin-bottom: 10px;
  }
  .Download-button:hover {
    background-color: rgb(44,43,43);
    color: white;
  }

  .Apply-button {
    height: 30px;
    width: 190px;
    border-radius: 15px;
    background-color: rgb(3,115,220);
    color: white;
    cursor: pointer;
    border: solid 1px rgb(5,13,90);
    transition: background-color 0.5s;
    margin-right: 10px;
    margin-bottom: 10px;
  }
  .Apply-button:hover { background-color: rgb(1,59,158); }

  .Save-button {
    height: 35px;
    width: 70px;
    background-color: white;
    color: rgb(36,85,233);
    border: solid 1.5px rgb(36,85,233);
    border-radius: 45px;
    font-weight: bold;
    transition: background-color 0.5s;
  }
  .Save-button:hover { background-color: rgba(152,189,240,0.436); }
</style>

<button class="Request-button">Request now</button>
<button class="Addtocart-button">Add to Cart</button>
<button class="signup-button">Sign up</button>
<button class="getstarted-button">Get started</button>
<button class="Download-button">Download</button>
<button class="Apply-button">Apply on company website</button>
<button class="Save-button">Save</button>
<a href="https://www.amazon.com/">Back to Amazon</a>
<p>Nike Black Running Shoes</p>
<p>$39 – in stock.</p>
<p>Free delivery tomorrow.</p>
<button>Add to Cart</button>
<button>Buy now</button>


💡 Learnings & Reflections

✅ Understood HTML structure and CSS linking
✅ Practiced transitions, hover states, shadows
✅ Improved understanding of button interactions
⚙️ Next Goal → Work on CSS Layout (Flexbox & Grid)

web-development/
└── day1-2/
    ├── 1a.html
    ├── 1b.html
    ├── 1c.html
    ├── buttons.html
    ├── exercises.html
    ├── hovers.html
    ├── transitions.html
    ├── shadows.html
    └── README.md

💬 “Build small UIs every day — mastery is a collection of tiny projects.”
