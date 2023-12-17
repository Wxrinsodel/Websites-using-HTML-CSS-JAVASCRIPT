let speech = new SpeechSynthesisUtterance();

let voices = []; //storing the available voices.

let voiceSelect = document.querySelector("select"); //being able to use a dropdown icon to choose different voice

window.speechSynthesis.onvoiceschanged = () => {
    voices = window.speechSynthesis.getVoices(); //Fetches the available voices.
    speech.voice = voices[0]; //Setting the default voice to the first voice in the list.
    
    voices.forEach((voice, i) => (voiceSelect.options[i] = new Option (voice.name, i)));
};

voiceSelect.addEventListener("change",() =>{
    speech.voice = voices[voiceSelect.value];
});

document.querySelector("button").addEventListener("click", () =>{
    speech.text = document.querySelector("textarea").value; // Setting the text to be spoken to the content of the textarea.
    window.speechSynthesis.speak(speech);

})