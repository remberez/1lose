import { useState } from 'react';

export default function ExpandableBlock({ eventData, onEventClick }) {
  const [isOpen, setIsOpen] = useState(false);

  const toggleOpen = () => setIsOpen(!isOpen);

  return (
    <div className="w-full mx-auto border rounded-md shadow p-2 bg-white font-inter">
      <div 
        onClick={toggleOpen} 
        className="cursor-pointer text-base font-bold text-gray-800 flex justify-between items-center"
      >
        <span>{ eventData.name }</span>
        <span className="text-blue-500">{isOpen ? '▲' : '▼'}</span>
      </div>

      {isOpen && (
        <div className="flex justify-between gap-x-2 mt-2">
          <button className="flex text-sm justify-between items-center p-1 bg-gray-200 rounded-md flex-1 hover:bg-gray-300" onClick={() => onEventClick(eventData.first_outcome)}>
            <span className="text-black">{ eventData.first_outcome?.name }</span>
            <span className="text-gray-700">{ eventData.first_outcome?.coefficient }</span>
          </button>
          <button className="flex text-sm justify-between items-center p-1 bg-gray-200 rounded-md flex-1 hover:bg-gray-300" onClick={() => onEventClick(eventData.second_outcome)}>
            <span className="text-black">{ eventData.second_outcome?.name }</span>
            <span className="text-gray-700">{ eventData.second_outcome?.coefficient }</span>
          </button>
        </div>
      )}
    </div>
  );
}
