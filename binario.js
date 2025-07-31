let basesBinario = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
basesBinario = basesBinario.reverse()
let numeroEscolhido = 1000
let numeroBinario = []

for (let i = 0; i < 10; i++) {

    if (numeroEscolhido >= basesBinario[i]) {
        numeroBinario.push(1)
        numeroEscolhido -= basesBinario[i]
    } else {
        numeroBinario.push(0)
    }
}
console.log(numeroBinario.join(" "))