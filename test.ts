
import * as fs from 'fs';

// Define the file path
const filePath: string = './src/questions/italianTranslation.json';

// Read the JSON file
fs.readFile(filePath, 'utf8', (err: NodeJS.ErrnoException | null, data: string | Buffer) => {
  if (err) {
    console.error(`Error reading the file: ${err.message}`);
    return;
  }

  try {
    // Parse the JSON data
    const jsonContent = JSON.parse(data.toString());

    // Print the JSON data to the console
    console.log(jsonContent);
  } catch (jsonError) {
    console.error(`Error parsing JSON: ${jsonError}`);
  }
});
