import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { analyze } from '@gege-mn/gege-converter';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const tsevelPath = path.join(rootDir, 'data', 'tsevel', 'monmon.txt');
const outputPath = path.join(rootDir, 'data', 'bichig_mapping.json');

console.log('[*] Reading Tsevel dictionary entries...');
const raw = fs.readFileSync(tsevelPath);
const parts = raw.toString('utf-8').split('\0');

const uniqueWords = new Set();
for (let i = 0; i < parts.length - 1; i += 2) {
    const rawWord = parts[i].trim();
    if (!rawWord) continue;
    
    // Clean base words: e.g. "ааг i" -> "ааг", "морь, морин" -> "морь", "морин"
    const cleaned = rawWord.replace(/\s+(?:[iIvVxX]+|\d+)$/, '').trim();
    if (cleaned) uniqueWords.add(cleaned);
    
    const subParts = rawWord.split(/[,/]/);
    for (const p of subParts) {
        const subClean = p.replace(/\s+(?:[iIvVxX]+|\d+)$/, '').trim();
        if (subClean) uniqueWords.add(subClean);
    }
}

console.log(`[+] Found ${uniqueWords.size.toLocaleString()} unique Mongolian words to convert.`);

const mapping = {};
let convertedCount = 0;
const t0 = Date.now();

for (const word of uniqueWords) {
    // Only convert pure cyrillic words
    if (!/^[\u0400-\u04FF\u0500-\u052F\-]+$/.test(word)) continue;
    
    try {
        const res = analyze(word);
        const topCandidate = res[0]?.candidates?.[0];
        if (topCandidate && topCandidate.script) {
            mapping[word] = {
                s: topCandidate.script,
                g: topCandidate.classical || ''
            };
            convertedCount++;
        }
    } catch {
        // Skip unconvertible tokens
    }
}

const elapsedSec = ((Date.now() - t0) / 1000).toFixed(1);
console.log(`[+] Successfully converted ${convertedCount.toLocaleString()} words in ${elapsedSec}s.`);

fs.writeFileSync(outputPath, JSON.stringify(mapping));
const fileSizeMB = (fs.statSync(outputPath).size / (1024 * 1024)).toFixed(2);
console.log(`[+] Wrote mapping to ${outputPath} (${fileSizeMB} MB)`);
