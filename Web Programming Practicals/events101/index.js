'use strict';
/**
 * Add your functions here...
 */

function targetTextToConsole(event) {
    console.log(event.target.textContent);
}

function tttcAttacher() {
    const button = document.querySelector('#button0');
    button.addEventListener('click', targetTextToConsole);
}

function lovelyParaAttacher() {
    const paragraph = document.querySelector('#thisisalovelyparagraph');
    paragraph.addEventListener('click', lovelyToggle);
}

function lovelyButtonAttacher() {
    const button = document.querySelector('#button1');
    button.addEventListener('click', lovelyToggle);
}

function concatAttacher() {
    const input1 = document.querySelector('#in1');
    const input2 = document.querySelector('#in2');
    const output = document.querySelector('#out1');
    function updateData() {
        output.innerText = input1.value + input2.value;
    }
    input1.addEventListener('change', updateData);
    input2.addEventListener('change', updateData);
}

function snitchAttacher() {
    const watcher = document.querySelector('#mousewatcher');
    const snitch = document.querySelector('#snitch');
    watcher.addEventListener('mouseover', () => {
        snitch.innerText = 'IN';
    });
    watcher.addEventListener('mouseout', () => {
        snitch.innerText = 'OUT';
    });
}

function reportAttacher() {
    const reporter = document.querySelector('#mousereporter');
    reporter.addEventListener('mousemove', reportUpdater);
}

function reportUpdater(event) {
    const report = document.querySelector('#report');
    report.innerText = `x: ${event.screenX} y: ${event.screenY}`;
}

function idValidationAttacher() {
    const newId = document.querySelector('#newid');
    newId.addEventListener('input', () => {
        if ((newId.value).includes(' ')) {
            newId.classList.add('invalid');
        } else {
            newId.classList.remove('invalid');
        }
    });
}
