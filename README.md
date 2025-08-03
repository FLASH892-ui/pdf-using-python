Flipkart database XML to PDF (Beginner Python Project):

Hi! I'm currently learning C++ (OOP & DSA), and this is one of my first hands-on projects in Python. Here's how it started:

The Backstory:

I had a college assignment to write an XML structure for a Flipkart database. I was running out of time, so I asked ChatGPT to help me generate a PDF for submission.

Initially, it gave me the PDF directly — but generating PDF files requires a premium plan, which I didn’t have. So I decided to dig into the source code of the generated PDF instead.

To my surprise, I found some familiar Python syntax (I had only learned Python basics). I got curious — Can I do this myself?)

And that's when the journey began...

Steps I Followed:

STEP 1 — Create a Project Folder:

Made a new folder in my system to keep everything organized.

STEP 2 — Add XML Files:

I created:

flipkart_input.xml — the XML input

flipkart_output.xml — the expected output (although later I used screenshots instead)

STEP 3 — Add DejaVu Font:

Python's fpdf module requires a Unicode-supported font to avoid encoding errors. I downloaded DejaVuSans.ttf and placed it in the same folder.

This part was a little tricky — but I learned how important fonts are when dealing with Unicode content like XML.

STEP 4 — Customize Output Section:

Instead of just dumping the raw XML output, I wanted to make it visually stand out.

So, I took a screenshot of the browser-rendered XML (which has collapsible arrows and better structure) and added that as an image to the PDF.

STEP 5 — Write Python Script:

With the help of ChatGPT, I wrote the .py script using fpdf. After some tweaking and testing, the PDF was generated successfully! 

What I Learned:

How to use fpdf to generate PDF files with custom formatting...

How to embed XML, images, and Unicode content properly...

Why fonts like DejaVu are essential when dealing with non-ASCII characters...

The joy of automating boring stuff 😄

Reflection:

I could have written the whole thing manually…
But writing code to generate it made it so much more fun!

Honestly, after this experience, I feel way more excited to learn Python.
And yeah... it’s kind of making C++ feel a little less fun right now 😂😂

Technologies Used:

...Python 3

...FPDF library (fpdf)

...DejaVuSans.ttf (Unicode font)

...Screenshots of browser-rendered XML

...VS Code + Windows PowerShell

Final Note:
I'm just a beginner, but this mini project taught me more than a week of theory ever could. If you're also learning Python or transitioning from C++, I hope this inspires you to build something — no matter how small.
