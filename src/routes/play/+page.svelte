<script>
    import Content from "./Content.svelte";

    let defSet = {word: "egotism", fos: "n.", def: "thinking only about yourself and considering yourself better and more important than other people."}

    let userInput;

    let correct = 0;

    function check() {
        document.getElementById("userInput").disabled = true;
        if (userInput.trim() === defSet.word) {
            correct = 1;
        } else {correct = -1}
    }

    function newWord() {
        console.log("new!")
    }

    function userSubmit() {
        if (correct === 0) {
            check()
        } else {
            newWord()
        }
    }
</script>

<div class="h-screen w-screen inter bg-zinc-200 text-zinc-950 flex flex-col items-center justify-center">
    <Content defSet={defSet} hide={correct === 0} correct={correct}/>

    <div id="inputs" class="mt-12
                            w-80 sm:w-96
                            flex flex-row items-center justify-center">
        <input id="userInput" bind:value={userInput} class="bg-zinc-50 h-8 sm:h-10 w-48 sm:w-72 border-2 border-zinc-600 px-2 mr-2 jbm text-base" placeholder="enter word..."/>
        <button id="check" class="bg-zinc-50 px-1.5 h-full border-2 border-zinc-600" on:click={userSubmit}>-> {correct===0?"Check":"Next"}</button>
    </div>
</div>