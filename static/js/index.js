const numberPad = document.getElementById('number-pad');

const context = numberPad.getContext('2d');
context.lineCap = 'round';

const lineWidthRange = document.getElementById('line-range');
const lineWidthLabel = document.getElementById('range-value');

const guessNumberBtn = document.getElementById('guess-number');
const resetCanvasBtn = document.getElementById('reset-canvas');

const canvasContainer = document.getElementById('canvas-container');

let isMouseDown = false;
let drewOnCanvas = false;
let x = 0, y = 0;

lineWidthRange.addEventListener('input', event => {
  const width = event.target.value;
  lineWidthLabel.innerHTML = width;
  context.lineWidth = width;
});

const guessNumber = () => {
  const img = numberPad.toDataURL('image/png');
  const formData = new FormData();
  formData.append('canvas_image', img);

  fetch('post_drawing', {
    method: 'POST',
    body: formData
  })
    .then(response => response.text())
    .then(result => updatePredictedDigit(result))
    .catch(error => console.error('Error:', error));
}

const resetCanvas = () => {
  context.clearRect(0, 0, numberPad.width, numberPad.height);
  guessNumberBtn.classList.replace('block', 'hidden');
  resetCanvasBtn.classList.replace('block', 'hidden');
  canvasContainer.classList.replace('max-h-[29rem]', 'max-h-[23rem]');

  drewOnCanvas = false;
  predictedDigitElement.innerText = 'Draw image on canvas to predict digit';
}

const stopDrawing = () => isMouseDown = false;

const startDrawing = (event) => {
  isMouseDown = true;
  [x, y] = [event.offsetX, event.offsetY];
}

const drawLine = (event) => {
  if (isMouseDown) {
    const newX = event.offsetX;
    const newY = event.offsetY;

    context.beginPath();
    context.moveTo(x, y);
    context.lineTo(newX, newY);
    context.stroke();

    x = newX;
    y = newY;

    if (!drewOnCanvas) {
      drewOnCanvas = true;
      guessNumberBtn.classList.replace('hidden', 'block');
      resetCanvasBtn.classList.replace('hidden', 'block');
      canvasContainer.classList.replace('max-h-[23rem]', 'max-h-[29rem]');
    }
  }
}

/**
 * Updates the UI with the predicted digit.
 * 
 * @param {number} digit
 */
const updatePredictedDigit = (digit) => {
  const predictedDigitElement = document.getElementById('predicted-digit');

  predictedDigitElement.innerText = `Your predicted digit is ${digit}`;
}

numberPad.addEventListener('mousedown', startDrawing);
numberPad.addEventListener('mousemove', drawLine);
numberPad.addEventListener('mouseup', stopDrawing);
numberPad.addEventListener('mouseout', stopDrawing);

guessNumberBtn.addEventListener('click', guessNumber);
resetCanvasBtn.addEventListener('click', resetCanvas);
