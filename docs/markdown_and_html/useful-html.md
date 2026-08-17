---
title: Useful HTML
icon: material/xml
date: 2026-08-16
---




## Linux Centered Banner
<div style="position:relative;width:min(600px, 100%);height:100px;margin:2rem auto;display:flex;align-items:center;justify-content:center;border-radius:.375rem;overflow:hidden;background-image:url('https://picsum.photos/600/100?random=1&grayscale');background-repeat:no-repeat;background-size:cover;background-position:center;">
    <div style="position:absolute;inset:0;background:rgba(253, 21, 21, 0.15);z-index:0;"></div>
    <img src="/img/linux/tux.svg" alt="linux" style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;"/>
    <img src="/img/linux/tux-pipe.svg" alt="linux" style="position:relative;z-index:1;width:5rem;margin:.5rem;opacity:.8;"/>
    <img src="/img/linux/tux-hat.svg" alt="linux" style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;"/>
</div>

My favorite little custom Linux banner, just to add a little fubtle flair. 

It will pull in a random grayscale background, tint it a color, and add images equally spaced. Everything should be pretty centered all around.

You can manipulate the size of the icons a little to create more of an effect (see above with middle icon larger).

```html
<div class="headercontainer" style="background-image: url('https://picsum.photos/600/100?random=1&grayscale');">
    <img class="headercontainericon" src="{{ $logoPath1 | relURL }}" alt="linux"/>
    <img class="headercontainericon" src="{{ $logoPath2 | relURL }}" alt="linux"/>
    <img class="headercontainericon" src="{{ $logoPath3 | relURL }}" alt="linux"/>
</div>
```

```css
.headercontainer {
  position:relative;
  width:min(600px, 100%);
  height:100px;
  margin:2rem auto;
  display:flex;
  align-items:center;
  justify-content:center;
  border-radius:.375rem;
  overflow:hidden;
  background-repeat:no-repeat;
  background-size:cover;
  background-position:center;
}

.headercontainer::after{
  content:"";
  position:absolute;
  inset:0;
  background: rgba(253, 21, 21, 0.15); /* tweak or delete */
  z-index:0;
}

.headercontainericon { 
    position:relative; 
    z-index:1; 
    height:4rem;
    width:auto;
    max-width:5rem;
    margin:.5rem; 
    opacity: .8; 
}
```



All-in-One:
```html
<div style="position:relative;width:min(600px, 100%);height:100px;margin:2rem auto;display:flex;align-items:center;justify-content:center;border-radius:.375rem;overflow:hidden;background-image:url('https://picsum.photos/600/100?random=1&grayscale');background-repeat:no-repeat;background-size:cover;background-position:center;">
    <div style="position:absolute;inset:0;background:rgba(253, 21, 21, 0.15);z-index:0;"></div>
    <img src="/img/linux/linux.svg" alt="linux" style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;"/>
    <img src="/img/linux/linux-black.svg" alt="linux" style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;"/>
    <img src="/img/linux/linux-white.svg" alt="linux" style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;"/>
</div>
```

<div style="position:relative;
            width:min(600px, 100%);
            height:100px;
            margin:2rem auto;
            display:flex;
            align-items:center;
            justify-content:center;
            border-radius:.375rem;
            overflow:hidden;background-image:url('https://picsum.photos/600/100?random=1&grayscale');
            background-repeat:no-repeat;background-size:cover;background-position:center;">
    <div style="position:absolute;
                inset:0;
                background:rgba(253, 21, 21, 0.15);
                z-index:0;">
    </div>
    <img style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;" src="/img/linux/linux-white.svg" alt="linux"/>
    <img style="position:relative;
                z-index:1;
                width:5rem;
                margin:.5rem;
                opacity:.8;" 
         src="/img/linux/linux.svg" alt="linux"/>
    <img style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;" src="/img/linux/linux-black.svg" alt="linux"/>
</div>