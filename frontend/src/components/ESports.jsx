import React, { useEffect, useState } from "react";
import gameService from "../services/gameService";
import matchService from "../services/matchService";

const esports = [
  { name: "Live", events: 120, color: "from-pink-500 to-red-500", icon: "🎮" },
  { name: "CS2", subtitle: "Шутер", icon: "🔫" },
  { name: "Dota 2", subtitle: "MOBA", icon: "🧙" },
  { name: "Valorant", subtitle: "Тактический шутер", icon: "🎯" },
  { name: "League of Legends", subtitle: "MOBA", icon: "🐉" },
  { name: "Overwatch 2", subtitle: "Шутер", icon: "🛡️" },
];

const EsportsCategories = () => {
  const [esports, setEsports] = useState([]);

  useEffect(() => {
    async function getEsports() {
      const esportsData = await gameService.getGames();
      setEsports(esportsData);
    }

    getEsports();
  }, []);
  return (
    <section>
      <h2 className="text-2xl font-bold mb-4">Киберспорт</h2>
      <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4">
        <div className="rounded-2xl shadow-md bg-gradient-to-br from-red-500 to-red-700 text-white p-4 flex flex-col justify-between h-32 transition-transform duration-200 hover:scale-105">
          <div className="text-4xl">
            🎮
          </div>
          <div>
            <p className="font-semibold text-lg leading-tight">Live</p>
            <p className="text-xs mt-1 text-gray-300">120 событий</p>
          </div>
        </div>
        {esports.map((item, index) => (
          <div
            key={index}
            className={`rounded-2xl shadow-md bg-gradient-to-br ${
              item.color || "from-oneWinBlue-400 to-oneWinBlue-500"
            } text-white p-4 flex flex-col justify-between h-32 transition-transform duration-200 hover:scale-105`}
          >
            <img
              src={item.icon_path}
              width={50}
              height={50}
            />
            <div>
              <p className="font-semibold text-lg leading-tight">{item.name}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

const matches = [
    {
      teams: ["OG", "Metizport"],
      scores: [1, 2],
      odds: [2.35, 1.55],
      status: "Live",
      tournament: "Counter-Strike. BLAST.tv Austin Major",
    },
    {
      teams: ["TEAM NEXT LEVEL", "Sangal Esports"],
      scores: [5, 2],
      odds: [1.05, 7.70],
      status: "Live",
      tournament: "Counter-Strike. Galaxy Battle. Bo3",
    },
    {
      teams: ["Heroic", "Nemiga Gaming"],
      scores: [10, 11],
      odds: [1.11, 5.80],
      status: "Live",
      tournament: "Counter-Strike. BLAST.tv Austin Major",
    },
    {
      teams: ["Complexity Gaming", "Getting Info"],
      scores: [3, 5],
      odds: [1.15, 4.90],
      status: "Live",
      tournament: "Counter-Strike. BLAST.tv Austin Major",
    },
  ];
  
function EsportsMatchCards() {
  const [liveMatches, setliveMatches] = useState([]);

  useEffect(() => {
    async function getLiveGames() {
      const liveMatchesData = await matchService.getLiveMatches();
      setliveMatches(liveMatchesData);
      console.log(liveMatchesData)
    }
    getLiveGames();
  }, [])
    return (
      <div className="mt-4">
        <h2 className="text-2xl font-bold mb-4">Топ-события</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          {liveMatches?.map((match, index) => (
            <div
              key={index}
              className="bg-white shadow-md rounded-lg p-4 border border-gray-200"
            >
              <div className="text-xs text-purple-600 font-semibold mb-1">Киберспорт</div>
              <div className="text-sm text-gray-500 mb-2">{match?.tournament.name}</div>
  
              <div className="flex items-center justify-between mb-2">
                <div className="flex flex-col">
                  <span className="font-medium">{match?.first_team.name}</span>
                  <span className="font-medium">{match?.second_team.name}</span>
                </div>
                <div className="flex flex-col text-right">
                  <span className="text-lg font-bold text-gray-700">{match.score[0]}</span>
                  <span className="text-lg font-bold text-gray-700">{match.score[1]}</span>
                </div>
              </div>
  
              <div className="flex items-center justify-between text-sm mb-2">
                <span className="text-green-600 font-semibold">Live</span>
              </div>
  
              <div className="flex justify-between gap-2 mt-2">
                <button className="bg-gray-100 text-gray-800 py-1 px-2 rounded-md w-full">
                  {match?.win_event.first_outcome.coefficient}
                </button>
                <button className="bg-gray-100 text-gray-800 py-1 px-2 rounded-md w-full">X</button>
                <button className="bg-gray-100 text-gray-800 py-1 px-2 rounded-md w-full">
                  {match?.win_event.second_outcome.coefficient}
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
}

const MainPageEvents = () => {
    return (
        <div className="container shadow-xl p-4 mt-4 border rounded-xl">
            <EsportsCategories/>
            <EsportsMatchCards/>
        </div>
    )
}

export default MainPageEvents;