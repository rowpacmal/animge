import axios from 'axios';

async function responseHandler(url: string) {
  try {
    const response = await axios.get(url, { responseType: 'arraybuffer' });

    if (response.status === 200) {
      return response.data;
    } else {
      throw new Error(`Request failed with status: ${response.status}`);
    }
  } catch (error) {
    if (error instanceof Error) {
      console.error(error.message);
      throw error;
    } else {
      console.error(error);
      throw new Error('Unknown error');
    }
  }
}

export default responseHandler;
