# Rebuild Readme

## Visual Page Structure

Pretty simple, vertical structure. Has the nice side effect that I don't need to have stuff reposition to keep things responsive.

```
header                             nav
---------------hor line---------------

HEADLINE

content

---------------hor line---------------
footer                       web links
```


## Logical Page Structure

The content pages can be their own HTML.
The header and footer can be their own HTML and simply concatenated to each of the content pages.

Pseudo-Code:
```html
<header-with-nav/>
<content/>
<footer-with-links/>
```

Concatenation can be done with a small Typescript or Python script.
Links to other content pages can be done with simple hrefs to where the pages reside.


## Build Process & Directory Structure

Build process is simple:
 - take all .html files other than header.html and footer.html and concatenate with header and footer, then copy the result over to /build
 - take all .scss files, compile to .css if necessary, then copy them over to /build
 - take all /src/asset files, process, then copy over to /build/assets

Advantages:
 - hrefs, when used relative and not absolute, should point to their own "realm", so point to other pages within src and build respectively.
 - assed size/color depth reduction is automated
 - No html generation other than copying stuff

```
/
  `- build.py
/src
  `- styles.scss
  `- header.html
  `- discography.html
  `- ...
# contains original-res images
/src/assets
  `- awesome-peter.png
  `- ...
/build
  `- styles.scss
  `- header.html
  `- discography.html
  `- ...
# contains reduced-res images
/build/assets
  `- awesome-peter.png
```