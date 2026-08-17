---
title: How I Created a Resume with Markdown, HTML, and Bash
icon: material/book-open-blank-variant-outline
date: 2026-08-17
featured: true
---
# How I Created a Resume

Resume design can be hard. Too many ideas about what it should look like, how many pages, don't include that, be sure to include this...
The struggle is amplified in today's days wondering if a human will ever even lay eyes on the resume. Is all that hard work done in vain? (Yeah, probably)

For a long time now, I have used Google Slides to build a resume (the google docs powerpoint equivalent). I love the ability to place text in precise positions, add tables, add stylings. You can really pack a lot into a small page! Then just export it to a pdf. Done.

But eventually, I guess I couldn't help myself, I wanted to try building the same design in a better way.  Or as I like to do, over engineer something that already works.

What comes from this is probably not "better" in any way, but at least it's more predictable, and can be put in your back pocket to be edited easily and anywhere, without relying on google docs. 

The initial idea is simple: 
- Write it in Markdown
- Use a simple script to end up with a decent looking pdf

What resulted feels like over engineering to do a simple thing, but it was interesting and worth writing down nonetheless. And as usual, small little hiccups emerge at every turn.

## The Markdown

Markdown is great. Simple, easy to plug and play. Easy to pick up a year later and figure out where things should go. 

However, my "slides resume" uses a lot of tables. I like tables. Structured, predictable, you can do a lot on the HTML side...not so much on the Markdown side. 

the good news: You can add html in your markdown!
the bad news: It's a little more messy having html tags everywhere.

We want to do stuff like add color, merge cells, and stuff like that. 
Suddenly we need css. Ugh, getting messier fast.

I won't bore with the css details, but we can add style tags directly in the markdown. 
```html
<style>
  @page { size: A4; margin: 2mm; }   /* or A4 */
  html, body { margin:0 !important; padding:0 !important; max-width:none !important; font-family: "Libre Caslon Text", serif; font-size: .9rem;}
  .markdown-body, .resume, main, article, section {
    margin:0 !important; padding:0 !important; max-width:none !important; width:auto !important;
  }

  * { box-sizing: border-box; }
  table { width:100% !important; border-collapse:collapse; table-layout:fixed; display:table !important; }
  td, th { word-break:break-word; }

  /* Utilities */
  .spread { display:flex; justify-content:space-between; }
  .right  { text-align:right }
  .center { text-align:center }

  /* Job table base */
  .job { width:100%; table-layout:fixed;  color: #000; border-top: none; border-bottom: none; }
  .job col:nth-child(1){ width:30% }
  .job col:nth-child(2){ width:30% }
  .job col:nth-child(3){ width:20% }
  .job col:nth-child(4){ width:20% }
  .job td { padding:4px 6px; vertical-align:top;  border-top: none; border-bottom: none; }

  /* Variants */
  .job--primary   { background: #af3fa6ff; border-bottom:4px solid #a32424ff; }
  .job--secondary { background: #bb8de3;   border-bottom:4px solid #a32424ff; }
  .job--other { background: #867b91ff;   border-bottom:4px solid #a32424ff; }
  /* Headers */
  h1, h2 {
    border-bottom: none !important;
    text-decoration: none !important;
    padding-bottom: 0;   /* some themes add spacing for the border */
    margin-bottom: .4em; /* tweak if spacing now feels off */
  }
  .contact { width:100%; border-collapse:collapse; table-layout:fixed; }
  .contact col.r    { width:12% }
  .contact col.name { width:28% }
  .contact td { padding:2px 6px; vertical-align:middle; white-space:nowrap }
  .contact .name { font-size:1.6rem; font-weight:700; line-height:1.1 }
  .contact tr.right > td { text-align:right }  /* <-- right-justify rows 2–3 */
  .icon { height:14px; width:auto; vertical-align:middle; background: white; }

    /* Code / long text should wrap, not overflow */
  pre, code, tt, kbd {
    white-space:pre-wrap !important;
    overflow-wrap:anywhere;
    word-break:break-word;
  }

  /* Added by AI below: keep entries from splitting awkwardly across page breaks */
  .job, li {
    break-inside: avoid-page;
    page-break-inside: avoid;
  }
  .job {
    break-after: avoid-page;   /* glue a job's title row to the bullets that follow it */
    page-break-after: avoid;
  }
  h1, h2, h3 {
    break-after: avoid-page;
    page-break-after: avoid;
  }
</style>
```

Not too bad, kinda long, it can stay on the top of the markdown page. At least we have everything on the page and we can change as needed. 

But now we have the tables. Which will inherit all the css properties. 
Other than making the simple markdown file ugly, tables are relatively straight forward.

### Header
We'll have a header table with all our personal metadata:
```html
<table class="contact">
  <colgroup>
    <col class="name">
    <col><col><col><col><col><col>
  </colgroup>
  <tr>
    <td class="name" rowspan="3">JJ</td>
    <td class="right" colspan="2">@gmail.com</td>
    <td class="right" colspan="2">555-555-5555</td>
    <td class="right" colspan="2">
      <img class="icon" src="./static/dcflag.svg" alt="DCFlag">
      <span>Washington, DC</span>
    </td>
  </tr>
  <tr class="right">
    <td colspan="2"></td>
    <td colspan="2">
      <img class="icon" src="./static/linkedin.svg" alt="Linkedin">
      <a href="https://linkedin.com/in/clementsjj">linkedin.com/in/clementsjj</a>
    </td>
    <td colspan="2">
      <span>&nbsp;</span>
      <img class="icon" src="./static/github.svg" alt="GitHub">
      <a href="https://github.com/clementsjj">github.com/clementsjj</a>
    </td>
  </tr>
  <tr class="right">
    <td colspan="2"></td>
    <td colspan="2">website1.tld</td>
    <td colspan="2">
      <img class="icon" src="./jjlogo.png" alt="jjlogo">
      <a href="https://jjserver.sh">jjserver.sh</a>
    </td>
  </tr>
</table>
```

Ugh, it's not pretty, but it will hopefully never have to change.
Add a little content below the header and we have a little introduction paragraph. 

There's one kinda huge bug here though...
It's the phone number. If you use 555-555-5555 then you won't have an issue. 
If you use the (555) style for area code, you do. And you can see the crazy SED pattern in the script below that addresses it. 

Click the notes box to learn more

> [!info]- Pandoc and Manipulating HTML
> > When you use (555) as an area code, pandoc will start to parse that 5) as markdown and screw up the formatting of EVERYTHING. 
> > 
> > So as a hack, around the header table in the markdown page, add:
> > ```markdown
> > <!-- REPLACE HTML TAG1 HERE --> TABLE HEADER STUFF <!-- REPLACE HTML TAG2 HERE -->
> > ```
> 
> Then in the script, we use SED to replace that with html which tells pandoc to render raw html, this way it won't pick up on special characters like `)` which switch it back to markdown rendering. 
> 
> Due to rendering code in this box thing, you will have to refer to the script below. Lood for a complicated SED command to see how it replaces the text.


### The Body

The body is pretty simple in theory. 
We want an html table with the job metadata, and then we can write out the bullet points in normal markdown text. 
And each job can have an html table. 

That will look like this: 

```html
### Professional Experience
<table class="job job--primary">
  <colgroup><col><col><col><col></colgroup>
  <tr>
    <td><b>Job Title</b></td>
    <td>Company</td>
    <td>Locatoin</td>
    <td class="right">Time Frame</td>
  </tr>
</table>
```

The only difference between the next job is the table class, we can change `job--primary` to change the color of the table with something like `job--secondary`.


## The HTML
Before converting to PDF, we will need to convert the markdown resume to html. This is to ensure we can flush out all the finer details, like where the page margin is. 
Luckily, this is handled by the script, and there's not any real intervention needed. 

I originally used `pandoc $TMP_MD -o $FILENAME.html --standalone` to convert, but the padding to the edge of the page was just not going to work, not with a resume where you need to maximize how you use your space. 

To get around this padding issue, we just have to construct the file a little differently. 

```bash
# Create minimal HTML wrapper without Pandoc's CSS
cat > "html_output/$FILENAME.html" << 'EOF'
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
EOF

# Convert markdown content with pandoc but without its default styling
pandoc "$TMP_MD" >> "html_output/$FILENAME.html"

# Close HTML
echo '</body></html>' >> "html_output/$FILENAME.html"
```

And that's it. This will be part of the script that builds it to the pdf finish line. 


## The PDF
This is also ran in the script covered in the next section. But once we have our html to the way we like it, the pdf conversion is pretty simple: 

```bash
chromium --headless --disable-gpu \
  --print-to-pdf="$PWD/pdf_output/$FILENAME.pdf" \
  --no-pdf-header-footer \
  "file://$PWD/html_output/$FILENAME.html"
```

Turns out chrome can print to pdf. 

## The Script
This is the piece that we want to bring us from the chill markdown file we created to the flushed out pdf. 

The file structure I have for this is as follows:
```
.
├── html_output
│   └── resume-technical.html
├── markdown_resume
│   └── resume-technical.md
├── md-to-pdf.sh
├── pdf_output
│   └── resume-technical.pdf
└── static
    ├── dcflag.svg
    ├── github.svg
    ├── jjlogo.png
    └── linkedin.svg
```

The script will allow you to select anything in the `markdown_resume` directory. 

The magic script is as follows: 

```bash
#!/usr/bin/env bash

MD_DIR="markdown_resume"

if [[ -n "$1" ]]; then
  # Allow passing a filename (with or without .md) directly, e.g.:
  #   ./md-to-pdf.sh resume-technical
  INPUT_FILE="${1%.md}"
else
  mapfile -t MD_FILES < <(find "$MD_DIR" -maxdepth 1 -name '*.md' -printf '%f\n' | sort)
  if [[ "${#MD_FILES[@]}" -eq 0 ]]; then
    echo "Error: no .md files found in $MD_DIR" >&2
    exit 1
  fi
  echo "Select input file from $MD_DIR:"
  select choice in "${MD_FILES[@]}"; do
    if [[ -n "$choice" ]]; then
      INPUT_FILE="${choice%.md}"
      break
    fi
    echo "Invalid selection, try again."
  done
fi

FILENAME="$INPUT_FILE"
TMP_MD="$(mktemp --suffix=.md)"

echo "Processing $INPUT_FILE.md"
echo "HTML output: html_output/$FILENAME.html"
echo "PDF output: pdf_output/$FILENAME.pdf"
echo "--------------------------------"

echo "Replacing HTML tags..."
# <!-- REPLACE HTML TAG1 HERE -->  => ```{=html}
# <!-- REPLACE HTML TAG2 HERE -->  => ```
sed -E \
  -e 's/<!--[[:space:]]*REPLACE[[:space:]]+HTML[[:space:]]+TAG1[[:space:]]+HERE[[:space:]]*-->/```{=html}/g' \
  -e 's/<!--[[:space:]]*REPLACE[[:space:]]+HTML[[:space:]]+TAG2[[:space:]]+HERE[[:space:]]*-->/```/g' \
  -- "$MD_DIR/$INPUT_FILE.md" > "$TMP_MD"

opens=$(grep -c '```{=html}$' "$TMP_MD" || true)
closes=$(grep -c '^```$' "$TMP_MD" || true)
if [[ "$opens" -ne "$closes" ]]; then
  echo "Error: unmatched fences after substitution (open=$opens close=$closes)" >&2
  exit 1
fi

echo "Creating HTML wrapper..."
# Create minimal HTML wrapper without Pandoc's CSS
cat > "html_output/$FILENAME.html" << 'EOF'
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
EOF

echo "Converting markdown to HTML..."
# Convert markdown content with pandoc but without its default styling
pandoc "$TMP_MD" >> "html_output/$FILENAME.html"

echo "Closing HTML wrapper..."
# Close HTML
echo '</body></html>' >> "html_output/$FILENAME.html"

echo "Printing to PDF..."
chromium --headless --disable-gpu \
  --print-to-pdf="$PWD/pdf_output/$FILENAME.pdf" \
  --no-pdf-header-footer \
  "file://$PWD/html_output/$FILENAME.html"
```


Run `chmod +x ./md-to-pdf.sh`, and kick it off `./md-to-pdf.sh`.

The resume will output in the `pdf_output` directory.

