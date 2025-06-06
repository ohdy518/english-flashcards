<script>
    export let defSet;
    export let hide;
    export let correct;
</script>

<div class="bg-zinc-50
            w-80 sm:w-120 h-48 sm:h-72
            text-base sm:text-lg
            border-3 {correct===0?'border-zinc-950':(correct===1?'border-green-500':'border-rose-500')} rounded-lg flex flex-col items-center justify-center ssr">
    <span class="font-bold text-lg sm:text-2xl pb-6 {hide?'hidden':'visible'}">egotism</span>
    <div class="max-w-64 sm:max-w-96">
        <span class="italic rounded-lg bg-zinc-200 text-zinc-700 px-1.5">{defSet.fos}</span>
        <span class="font-semibold text-balance">{defSet.def}</span>
    </div>
</div>
