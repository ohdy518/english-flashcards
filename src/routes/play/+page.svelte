<script>
    import Content from "./Content.svelte";
    import {words} from "$lib/wordlist.js";
    import {browser} from "$app/environment";

    let totalLen = words.length;

    // console.log(words)

    let localWords = words
    localWords = shuffleArray(localWords);

    // console.log(localWords)

    let defSet = {word: "Wait...", fos: "!", def: "please wait..."}

    let wrongList = []

    let userInput;

    let correct = 0;
    if (browser) {
        newWord()
    }

    function check() {
        if (userInput === "" || !userInput) {return}

        console.log(userInput);

        console.log("check invoked");

        document.getElementById("userInput").disabled = true;
        if (userInput.trim() === defSet.word) {
            correct = 1;
        } else {
            correct = -1
            wrongList.push(defSet);
        }

        document.addEventListener('keypress', handleEnterKey);
    }

    function newWord() {
        console.log("new!")
        document.removeEventListener('keypress', handleEnterKey);
        if (localWords.length > 0) {
            defSet = localWords.pop()
            correct = 0
        } else {
            defSet = {word: "finished!", fos: "!", def: (wrongList.length > 0 ? "review words answered incorrectly?" : "you got everything correct.")};
            correct = 1
            showReviewButton()
        }

        if (document.getElementById("userInput")) {
            document.getElementById("userInput").value = ""
            userInput = ""
            document.getElementById("userInput").disabled = false;
            document.getElementById("userInput").focus()
        }
    }

    function showReviewButton () {
        document.getElementById("form").hidden = true;
        if (wrongList.length > 0) {
            document.getElementById("review-button").hidden = false;
        }
    }

    function startReview() {
        defSet = {word: "Wait...", fos: "!", def: "please wait..."}
        correct = 0

        document.getElementById("review-button").hidden = true;
        document.getElementById("form").hidden = false;
        localWords = wrongList;
        totalLen = wrongList.length;
        wrongList = []

        newWord()

        document.getElementById("userInput").value = ""
        userInput = ""
        document.getElementById("userInput").disabled = false;
        document.getElementById("userInput").focus()

    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
        return array;
    }

    function handleEnterKey(event) {
        if (event.key === 'Enter') {
            newWord();
        }
    }

    function userSubmit() {
        console.log("userSubmit!")
        if (userInput === "" || !userInput) { document.getElementById("userInput").focus(); return}

        if (correct === 0) {
            check()
        } else {
            newWord()
        }
    }
</script>

<div class="h-screen w-screen inter bg-zinc-200 text-zinc-950 flex flex-col items-center justify-center">
    <span class="mb-3 font-semibold">{totalLen - localWords.length} of {totalLen}; {wrongList.length?wrongList.length:'nothing'} to review</span>
    <Content defSet={defSet} hide={correct === 0} correct={correct}/>

    <form id="form" class="mt-12
                            w-80 sm:w-96
                            flex flex-row items-center justify-center">
        <input id="userInput" bind:value={userInput} class="bg-zinc-50 h-8 sm:h-10 w-48 sm:w-72 border-2 border-zinc-600 px-2 mr-2 jbm text-base" placeholder="enter word..."/>
        <button id="check" class="bg-zinc-50 px-1.5 h-full border-2 border-zinc-600" on:click={userSubmit}>-> {correct===0?"Check":"Next"}</button>
    </form>
    <button id="review-button" class="mt-12 bg-zinc-50 px-1.5 h-8 border-2 border-zinc-600" on:click={startReview} hidden>-> Review</button>
</div>