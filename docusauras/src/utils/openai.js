// docusauras/src/utils/openai.js

import OpenAI from 'openai';

// IMPORTANT: Never expose your API key directly in client-side code for production.
// For a production application, you should proxy these requests through your backend (FastAPI).
// If you must use it client-side, consider environment variables injected at build time
// or a secure method to fetch it at runtime that does not expose it publicly.
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY, // Ensure this is securely loaded (e.g., from an environment variable)
  dangerouslyAllowBrowser: true, // This is required for client-side usage in non-standard environments.
                                 // Use with extreme caution and only if you fully understand the implications
                                 // of exposing your API key. Proxying through a backend is preferred.
});

/**
 * Generates embeddings for a given text using the OpenAI API.
 * @param {string} text The text to generate embeddings for.
 * @returns {Promise<number[]>} A promise that resolves to an array of embedding vectors.
 */
export async function generateEmbeddings(text) {
  if (!text) {
    console.warn("Attempted to generate embeddings for empty text.");
    return [];
  }

  try {
    const response = await openai.embeddings.create({
      model: "text-embedding-ada-002", // Or another suitable embedding model
      input: text,
    });
    return response.data[0].embedding;
  } catch (error) {
    console.error("Error generating embeddings:", error);
    throw error;
  }
}

// Example usage (for demonstration, remove from production code if not needed):
/*
(async () => {
  try {
    const textToEmbed = "The quick brown fox jumps over the lazy dog.";
    const embeddings = await generateEmbeddings(textToEmbed);
    console.log("Generated Embeddings (first 5 elements):", embeddings.slice(0, 5));
    console.log("Embeddings length:", embeddings.length);
  } catch (error) {
    console.error("Failed to generate embeddings in example:", error);
  }
})();
*/
