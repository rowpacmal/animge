function PromptBox({
  promptInput,
  setPromptInput,
}: {
  promptInput: string;
  setPromptInput: React.Dispatch<React.SetStateAction<string>>;
}) {
  return (
    <textarea
      className='border border-gray-300 rounded py-2 px-4 w-96'
      rows={4}
      value={promptInput}
      placeholder='Enter prompt...'
      onChange={(e) => setPromptInput(e.target.value)}
    />
  );
}

export default PromptBox;
