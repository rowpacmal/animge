import { useState } from 'react';
import responseHandler from '../utils/responseHandler';
import { MODEL, QUALITY_TAGS, STYLE_TAGS } from '../constants';

function useTextToImage() {
  const [generatedImage, setGeneratedImage] = useState<string | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  async function generateImage(
    prompt: string,
    width: number = 1024,
    height: number = 1024,
    seed: number = 0
  ) {
    if (!prompt) {
      setErrorMessage('Please enter a prompt');
      return;
    }

    setIsGenerating(true);
    setErrorMessage(null);

    try {
      const url = `https://image.pollinations.ai/prompt/Prompt:${QUALITY_TAGS.join()},${STYLE_TAGS.join()},${prompt}?model=${MODEL}&seed=${seed}&width=${width}&height=${height}&nologo=true`;
      const response = await responseHandler(url.replaceAll(' ', '%20'));

      if (response) {
        setGeneratedImage(response);
      }
    } catch (error) {
      console.error('Error generating image:', error);
      setErrorMessage('Failed to generate image');
    } finally {
      setIsGenerating(false);
    }
  }

  return {
    generatedImage,
    isGenerating,
    errorMessage,

    generateImage,
  };
}

export default useTextToImage;
