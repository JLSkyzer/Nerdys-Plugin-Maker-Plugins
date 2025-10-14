const fs = require('fs');
const path = require('path');

function processProcedureJSON(jsonPath) {
    try {
        const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
        let modified = false;

        if (data.versions && Array.isArray(data.versions)) {
            const has1214 = data.versions.includes('1.21.4_NeoForge');
            const has1211 = data.versions.includes('1.21.1_NeoForge');

            if (has1214) {
                if (has1211) {
                    // Remove 1.21.4_NeoForge if 1.21.1_NeoForge already exists
                    data.versions = data.versions.filter(v => v !== '1.21.4_NeoForge');
                    console.log(`  Removed 1.21.4_NeoForge from ${path.basename(jsonPath)}`);
                } else {
                    // Replace 1.21.4_NeoForge with 1.21.1_NeoForge
                    const idx = data.versions.indexOf('1.21.4_NeoForge');
                    data.versions[idx] = '1.21.1_NeoForge';
                    console.log(`  Replaced 1.21.4_NeoForge with 1.21.1_NeoForge in ${path.basename(jsonPath)}`);
                }
                modified = true;
            }
        }

        if (modified) {
            fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2), 'utf8');
        }

        return modified;
    } catch (e) {
        console.error(`  ERROR processing ${jsonPath}: ${e.message}`);
        return false;
    }
}

function processVariableJSON(jsonPath) {
    try {
        const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
        let modified = false;

        if (data.versions && typeof data.versions === 'object') {
            const has1214 = '1.21.4_NeoForge' in data.versions;
            const has1211 = '1.21.1_NeoForge' in data.versions;

            if (has1214) {
                if (has1211) {
                    // Remove 1.21.4_NeoForge if 1.21.1_NeoForge already exists
                    delete data.versions['1.21.4_NeoForge'];
                    console.log(`  Removed 1.21.4_NeoForge key from ${path.basename(jsonPath)}`);
                } else {
                    // Rename key from 1.21.4_NeoForge to 1.21.1_NeoForge
                    data.versions['1.21.1_NeoForge'] = data.versions['1.21.4_NeoForge'];
                    delete data.versions['1.21.4_NeoForge'];
                    console.log(`  Renamed 1.21.4_NeoForge to 1.21.1_NeoForge in ${path.basename(jsonPath)}`);
                }
                modified = true;
            }
        }

        if (modified) {
            fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2), 'utf8');
        }

        return modified;
    } catch (e) {
        console.error(`  ERROR processing ${jsonPath}: ${e.message}`);
        return false;
    }
}

function processCodeFiles(codeDir) {
    if (!fs.existsSync(codeDir)) {
        return;
    }

    const files = fs.readdirSync(codeDir);
    for (const file of files) {
        if (file.endsWith('1.21.4NeoForge.txt')) {
            const filePath = path.join(codeDir, file);
            const baseName = file.replace('1.21.4NeoForge.txt', '');
            const newName = baseName + '1.21.1NeoForge.txt';
            const newPath = path.join(codeDir, newName);

            if (fs.existsSync(newPath)) {
                // If 1.21.1 version exists, delete the 1.21.4 version
                fs.unlinkSync(filePath);
                console.log(`  Deleted ${file} (1.21.1 version already exists)`);
            } else {
                // Rename 1.21.4 to 1.21.1
                fs.renameSync(filePath, newPath);
                console.log(`  Renamed ${file} to ${newName}`);
            }
        }
    }
}

function processPlugin(pluginPath) {
    const pluginName = path.basename(pluginPath);
    console.log(`\nProcessing ${pluginName}...`);

    // Process procedures
    const proceduresDir = path.join(pluginPath, 'procedures');
    if (fs.existsSync(proceduresDir)) {
        console.log(`  Processing procedures JSON files...`);
        const files = fs.readdirSync(proceduresDir);
        for (const file of files) {
            if (file.endsWith('.json')) {
                processProcedureJSON(path.join(proceduresDir, file));
            }
        }

        // Process code files
        const codeDir = path.join(proceduresDir, 'code');
        if (fs.existsSync(codeDir)) {
            console.log(`  Processing code files...`);
            processCodeFiles(codeDir);
        }
    }

    // Process variables
    const variablesDir = path.join(pluginPath, 'variables');
    if (fs.existsSync(variablesDir)) {
        console.log(`  Processing variables JSON files...`);
        const files = fs.readdirSync(variablesDir);
        for (const file of files) {
            if (file.endsWith('.json')) {
                processVariableJSON(path.join(variablesDir, file));
            }
        }
    }
}

function main() {
    const baseDir = 'd:\\pluginbuilder_release_2.0\\plugins';
    const plugins = ['EriData', 'EriMap', 'EriObject', 'StringIndex', 'SkyzersPlugin'];

    console.log('Starting NeoForge version migration (1.21.4 -> 1.21.1)');
    console.log('='.repeat(60));

    for (const pluginName of plugins) {
        const pluginPath = path.join(baseDir, pluginName);
        if (fs.existsSync(pluginPath)) {
            processPlugin(pluginPath);
        } else {
            console.log(`\nWARNING: Plugin directory not found: ${pluginName}`);
        }
    }

    console.log('\n' + '='.repeat(60));
    console.log('Migration complete!');
}

main();
