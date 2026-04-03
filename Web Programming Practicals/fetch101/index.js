/*
 * This is index.js
 *
 * NB: all code you write this year should use strict mode, so
 * we've enabled that by default with the first line of code.
 */

'use strict';

async function showMessage(elem, url) {
  const response = await fetch(url);
  elem.textContent = await response.text();
}

async function showList(elem, url) {
  const response = await fetch(url);
  const data = await response.json();
  elem.innerHTML = '';
  data.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    elem.appendChild(li);
  });
}

function startShowingMessage(elem, url) {
  async function update() {
    const response = await fetch(url);
    elem.textContent = await response.text();
  }
  update();
  setInterval(update, 1000);
}

async function handleError(elem, url) {
  try {
    const response = await fetch(url);
    if (response.ok) {
      elem.textContent = await response.text();
    } else {
      throw new Error('HTTP error');
    }
  } catch {
    elem.textContent = 'OH DEAR';
  }
}

async function drawBox(canvas, url) {
  const box = canvas.getContext('2d');

  async function createBox() {
    const response = await fetch(url);
    const content = await response.json();
    box.fillStyle = content.color;
    box.fillRect(content.x, content.y, 10, 10);
  }

  await createBox();
  setInterval(createBox, 1000);
}
