let surveyInterval;
let elapsedSeconds = 0;
let totalCount = 0;
let surveyActive = false;

document.addEventListener('DOMContentLoaded', () => {
    const trafficLog = document.getElementById('traffic-log');
    if (trafficLog && trafficLog.tagName === 'TEXTAREA') {
        trafficLog.value = '';
        trafficLog.defaultValue = '';
        trafficLog.setAttribute('autocomplete', 'off');

        window.addEventListener('pageshow', (e) => {
            if (e.persisted) {
                trafficLog.value = '';
            }
        });

        window.addEventListener('beforeunload', () => {
            trafficLog.value = '';
        });
    }
});


function formatTime(seconds) {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${String(hrs).padStart(2, '0')}:${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}

function getTimestamp() {
    const now = new Date();
    const day = String(now.getDate()).padStart(2, '0');
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const year = now.getFullYear();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    return `[${day}/${month}/${year} ${hours}:${minutes}:${seconds}]`;
}

// javascript
function startSurvey() {
    if (surveyActive) return;

    const startTime = document.getElementById('start-time');
    if (startTime && (startTime.innerText === 'Start Time: N/A' || startTime.innerText.trim() === '')) {
        startTime.innerText = 'Start Time: ' + new Date().toLocaleString();
    }

    const endTime = document.getElementById('end-time');
    if (endTime) {
        endTime.innerText = 'End Time: N/A';
    }

    const isFirstStart = (elapsedSeconds === 0);

    surveyInterval = setInterval(() => {
        elapsedSeconds++;
        const timeCollecting = document.getElementById('time-collecting');
        if (timeCollecting) {
            timeCollecting.innerText = 'Time Collecting: ' + formatTime(elapsedSeconds);
        }
    }, 1000);

    const trafficLog = document.getElementById('traffic-log');
    if (trafficLog && trafficLog.tagName === 'TEXTAREA') {
        const entry = getTimestamp() + (isFirstStart ? ' - Survey Started' : ' - Survey Resumed');
        trafficLog.value = trafficLog.value ? trafficLog.value + '\n' + entry : entry;
        trafficLog.scrollTop = trafficLog.scrollHeight;
        trafficLog.selectionStart = trafficLog.selectionEnd = trafficLog.value.length;

        if (isFirstStart) {
            const lat = 50.8198;
            const lon = -1.0880;
            const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true&timezone=auto`;

            fetch(url)
                .then(response => {
                    if (!response.ok) throw new Error('Network response was not ok');
                    return response.json();
                })
                .then(data => {
                    let weatherEntry;
                    if (data && data.current_weather) {
                        const temp = Number(data.current_weather.temperature).toFixed(1);
                        const wind = Number(data.current_weather.windspeed).toFixed(1);
                        weatherEntry = `${getTimestamp()} - Weather in Portsmouth: ${temp}°C, wind ${wind} m/s`;
                    } else {
                        weatherEntry = `${getTimestamp()} - Weather in Portsmouth: unavailable`;
                    }
                    trafficLog.value = trafficLog.value ? trafficLog.value + '\n' + weatherEntry : weatherEntry;
                    trafficLog.scrollTop = trafficLog.scrollHeight;
                    trafficLog.selectionStart = trafficLog.selectionEnd = trafficLog.value.length;
                })
                .catch(() => {
                    const failEntry = `${getTimestamp()} - Weather in Portsmouth: unavailable`;
                    trafficLog.value = trafficLog.value ? trafficLog.value + '\n' + failEntry : failEntry;
                    trafficLog.scrollTop = trafficLog.scrollHeight;
                    trafficLog.selectionStart = trafficLog.selectionEnd = trafficLog.value.length;
                });
        }
    }

    surveyActive = true;
}

function stopSurvey() {
    if (!surveyActive) return;
    if (elapsedSeconds === 0) return;

    const startSurveyContainer = document.getElementById('start-survey');
    if (startSurveyContainer) {
        startSurveyContainer.style.display = 'block';
    }

    const startSurveyButton = document.getElementById('start-survey-btn');
    if (startSurveyButton) {
        startSurveyButton.innerHTML = '<i class="fa-solid fa-play"></i> Continue Survey';
    }

    const endTime = document.getElementById('end-time');
    if (endTime) {
        endTime.innerText = 'End Time: ' + new Date().toLocaleString();
    }

    const trafficLog = document.getElementById('traffic-log');
    if (trafficLog && trafficLog.tagName === 'TEXTAREA') {
        const entry = getTimestamp() + ' - Survey Stopped';
        trafficLog.value = trafficLog.value ? trafficLog.value + '\n' + entry : entry;
        trafficLog.scrollTop = trafficLog.scrollHeight;
        trafficLog.selectionStart = trafficLog.selectionEnd = trafficLog.value.length;
    }

    clearInterval(surveyInterval);

    surveyActive = false;
}

function addRecord() {
    if (!surveyActive) return;

    totalCount++;

    const totalCountElement = document.getElementById('total-count');
    if (totalCountElement) {
        totalCountElement.innerText = 'Total Count: ' + totalCount;
    }

    const trafficLog = document.getElementById('traffic-log');
    if (trafficLog && trafficLog.tagName === 'TEXTAREA') {
        const entry = getTimestamp() + ' - Record Added';
        trafficLog.value = trafficLog.value ? trafficLog.value + '\n' + entry : entry;
        trafficLog.scrollTop = trafficLog.scrollHeight;
        trafficLog.selectionStart = trafficLog.selectionEnd = trafficLog.value.length;
    }
}

function removeRecord() {
    if (!surveyActive || totalCount <= 0) return;

    totalCount--;

    const totalCountElement = document.getElementById('total-count');
    if (totalCountElement) {
        totalCountElement.innerText = 'Total Count: ' + totalCount;
    }

    const trafficLog = document.getElementById('traffic-log');
    if (trafficLog && trafficLog.tagName === 'TEXTAREA') {
        const entry = getTimestamp() + ' - Record Removed';
        trafficLog.value = trafficLog.value ? trafficLog.value + '\n' + entry : entry;
        trafficLog.scrollTop = trafficLog.scrollHeight;
        trafficLog.selectionStart = trafficLog.selectionEnd = trafficLog.value.length;
    }
}

function copyLog() {
    const trafficLog = document.getElementById('traffic-log');
    if (trafficLog && trafficLog.tagName === 'TEXTAREA') {
        trafficLog.select();
        document.execCommand('copy');
        trafficLog.selectionStart = trafficLog.selectionEnd = trafficLog.value.length;
    }
}

function exportLog() {
    const trafficLog = document.getElementById('traffic-log');
    if (trafficLog && trafficLog.tagName === 'TEXTAREA') {
        const blob = new Blob([trafficLog.value], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'survey_log.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
}