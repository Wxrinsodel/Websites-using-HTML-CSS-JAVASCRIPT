const display = document.querySelector("#display");
const buttons = document.querySelectorAll("button");

buttons.forEach((button) => {
  button.onclick = () => {
    handleButtonClick(button.id);
  };
});

function handleButtonClick(buttonId) {
  if (buttonId === "clear" || buttonId === "clear-entry") {
    display.innerText = "";
  } else if (buttonId === "delete") {
    let string = display.innerText.toString();
    display.innerText = string.substr(0, string.length - 1);
  } else if (display.innerText !== "" && buttonId === "equal") {
    display.innerText = evaluateExpression(display.innerText);
  } else if (display.innerText === "" && buttonId === "equal") {
    display.innerText = "Empty!";
    setTimeout(() => (display.innerText = ""), 2000);
  } else {
    display.innerText += buttonId;
  }
}

//taking a mathematical expression as a string
function evaluateExpression(expression) {
  return eval(expression);
}

//make a changing button relate to theme

const themeToggleBtn = document.querySelector(".theme-toggler");
const calculator = document.querySelector(".calculator");
const togglericon = document.querySelector(".toggler-icon");
togglericon.onclick = toggleDarkTheme;

themeToggleBtn.onclick = () => {
toggleDarkTheme();
};

function toggleDarkTheme() {
calculator.classList.toggle("dark");
themeToggleBtn.classList.toggle("active");
}
