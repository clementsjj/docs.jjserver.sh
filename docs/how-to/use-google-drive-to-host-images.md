---
title: How to Use Google Drive to Host Images for a Website"
description: "Get a link to a picture in google drive, and use it on a web page."
draft: false
tags: 
    - how-to
icon: material/book-open-blank-variant-outline
---

You have all sort of fantastic, raw photos stored on your google drive...now how do you use those images in a webpage?

You may have shared a folder or file with google drive before, copied the link, gave it to someone (or viceversa), and when you click to open the link you are brought to Google's lovely Drive ecosystem.

But what if you wanted just the picture itself, without behing wrapped up in the Google Drive ecosystem?


## Make Directory Shareable

First, move all images into a directory named "sharedimages", or whatever directory name will help you remember that anything in the folder is public.

Right click on `share`, under "General access", select `Anyone with the link`, and select Done.

## Find Shareable Link

If you right click on an image and select `Get link`. 
Select `Copy link`
Then paste the link somewhere to inspect..

https://drive.google.com/file/d/1li0yLTxPjILv7LqZoix66Hr0dhtIraCo/view?usp=share_link

We need to take this link, and turn it into this:

https://drive.google.com/uc?export=view&id=1li0yLTxPjILv7LqZoix66Hr0dhtIraCo

(In this particular instance, the image is in a subfolder of the main "shared folder". There is no need to specify the files location, the jumbled mess of characters is enough.)

## Use Bash to convert shareable link - method 1

```bash
#!/bin/bash
url=$1
new_url=$(echo $url | sed -e "s/file\/d\//uc?export=view\&id=/;")
echo "$new_url" | sed 's/\/view?usp=share_link//g'
```

This works great if you want to convert a single image.
But what about your whole inventory?

---

## Use Bash to convert shareable link - method 2
This method varies from method 1 in that you get the link from the image that is sourced when you view the image in the browser. Using a bash script, we can curl the "shareable" link, and then convert it to a "direct" link.


```bash
#!/bin/bash
url=$1
share_url=$(curl $url | grep -oP '(?<=<meta property="og:image" content=")[^"]*' | sed 's/\/view?usp=share_link//g')
echo $share_url
```

The difference here is that you can edit the size of the image.

Between the two methods, this would probably be the preferred based on the fact that you can edit the size of the image giving you a little bit of flexibility.


## Gather All Shareable Links
While there apparently is a way to gather all links in google sheets, I was having a hard time getting the script part to even load. Maybe google is deprecating it?

You can select all images in the folder, and right click to get the shareable link. You will recieve a link to each of the images selected.

### Use shareable links to get link of images
When you copy all shareable links, you get a list of links separated by a comma. 
Paste the list into a file. Save it as a whatever.txt file.
Then run the script to get a list of links to the images.

`bash create_list_from_shareable_links.sh whatever.txt`
```bash
#!/bin/bash
csv=$1
OUTPUT_FILE="output.txt"
printf "" > $OUTPUT_FILE
while IFS=, read -r line
do
    share_url=$(curl $line | grep -oP '(?<=<meta property="og:image" content=")[^"]*' | sed 's/\/view?usp=share_link//g')
    echo $share_url | tee -a $OUTPUT_FILE
done < "$csv"
```

