function App() {
  return (
    <div className='flex flex-col items-center justify-center h-screen gap-4'>
      <h1 className='text-3xl font-bold'>Animg AI</h1>

      <button
        className='bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded'
        onClick={() => console.log('Generate image')}
      >
        Generate
      </button>
    </div>
  );
}

export default App;
