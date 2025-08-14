import { useState } from 'react';
import responseHandler from '../utils/responseHandler';

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

    const model = 'flux';
    const qualityTags = [
      'masterpiece',
      'absurdres',
      'best quality',
      // 'perfect quality',
      // 'newest',
      // 'detailed background',
      // 'intricate details',
    ];
    const styleTags = ['anime style'];
    const negativeTags = [
      'lowres',
      'worst quality',
      'low quality',
      // 'bad anatomy',
      // 'bad hands',
      // 'missing fingers',
      // 'extra digit',
      // 'fewer digits',
      // 'cropped',
      // 'error',
      // 'blurry',
      // 'signature',
      // 'copyright',
      // 'watermark',
      // 'artist name',
      // 'text',
    ];

    try {
      const url = `https://image.pollinations.ai/prompt/Prompt:${qualityTags.join()},${styleTags.join()},${prompt}.Negative prompt:${negativeTags.join()}.?model=${model}&seed=${seed}&width=${width}&height=${height}&nologo=true`;

      console.log(url.replaceAll(' ', '%20'));

      const response = await responseHandler(url);

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
