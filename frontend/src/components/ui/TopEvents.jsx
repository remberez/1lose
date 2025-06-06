import { useEffect, useState } from 'react';
import { observer } from 'mobx-react-lite';
import { gamesStore } from '../../stores/games';
import { MatchesService } from '../../services/matches';
import Button from './Button';
import { Link } from 'react-router-dom';
import { GoDotFill } from "react-icons/go";

const TopEvents = observer(() => {
  const [selectedGame, setSelectedGame] = useState(null);
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [showLive, setShowLive] = useState(false);

  useEffect(() => {
    gamesStore.fetchGames();
  }, []);

  // Сброс выбранной игры при обновлении списка игр
  useEffect(() => {
    if (gamesStore.games.length && (selectedGame === null || !gamesStore.games.find(g => g.id === selectedGame))) {
      setSelectedGame(gamesStore.games[0].id);
    }
  }, [gamesStore.games]);

  // Загрузка событий при смене выбранной игры или фильтра Live
  useEffect(() => {
    if (!selectedGame) return;
    setLoading(true);
    setError(null);
    const filters = { game_id: selectedGame };
    if (showLive) filters.is_live = true;
    MatchesService.list(filters)
      .then(data => {
        setEvents(Array.isArray(data) ? data : []);
      })
      .catch(() => setError('Ошибка загрузки событий'))
      .finally(() => setLoading(false));
  }, [selectedGame, showLive]);

  return (
    <div className="container mx-auto px-4 my-8">
      <div className="flex items-center justify-start gap-x-4 mb-6">
        <h2 className="text-2xl font-bold text-black">Топ события</h2>
        <button
          className={`flex items-center gap-1 justify-start border border-gray-200 rounded-lg px-3 py-1 hover:bg-gray-100 transition-colors ${showLive ? 'bg-red-100 border-red-400' : ''}`}
          onClick={() => setShowLive(live => !live)}
        >
          <span>
            <GoDotFill color='red'/>
          </span>
          <span className="text-black font-semibold text-sm">
            Live
          </span>
        </button>
      </div>
      {/* Фильтрация по игре */}
      <div className="flex flex-wrap gap-2 mb-6">
        {gamesStore.games.map(game => (
          <Button
            key={game.id}
            className={`px-4 py-1 rounded-full text-sm font-semibold ${selectedGame === game.id ? 'bg-blue-700 text-white' : 'bg-blue-200 text-blue-900'}`}
            onClick={() => setSelectedGame(game.id)}
          >
            {game.name}
          </Button>
        ))}
      </div>
      {/* Сетка событий */}
      {loading ? (
        <div className="text-center py-8">Загрузка событий...</div>
      ) : error ? (
        <div className="text-center text-red-400 py-8">{error}</div>
      ) : (
        <div className="grid grid-cols-4 grid-rows-2 gap-4">
          {events.slice(0, 8).map(event => {
            // Коэффициенты (пример: event.odds = { win1: 2.08, draw: null, win2: 1.75 })
            const odds = event.win_event || {};
            return (
              <Link
                key={event.id}
                to={`/match/${event.id}`}
                className="bg-blue-50 rounded-xl p-0 flex flex-col items-stretch justify-between min-h-[170px] shadow border border-blue-100 relative overflow-hidden transition-transform hover:scale-[1.03]"
                style={{ minWidth: 0 }}
              >
                {/* Верхняя строка */}
                <div className="flex items-center gap-2 px-3 pt-2 pb-1">
                  <span className="bg-blue-200 text-blue-900 text-xs font-bold rounded px-2 py-0.5">Киберспорт</span>
                  <span className="text-xs text-blue-700 truncate font-medium">{event.tournament?.game?.name || ''}</span>
                  <span className="text-xs text-blue-400 truncate">{event.tournament?.name || ''}</span>
                  <span className="ml-auto text-gray-400 cursor-pointer">★</span>
                </div>
                {/* Команды и время/Live */}
                <div className="flex items-center justify-between px-3 py-2">
                  <div className="flex flex-col items-center w-16">
                    <img src={event.first_team?.icon_path} alt={event.first_team?.name} className="w-10 h-10 rounded-full bg-white object-contain mb-1" />
                    <span className="text-xs font-semibold text-blue-900 text-center truncate w-full">{event.first_team?.name}</span>
                  </div>
                  <div className="flex flex-col items-center w-24">
                    {(() => {
                      // Проверка: если сейчас между date_start и date_end (или если date_end нет, то date_start < now < date_start+3ч)
                      const now = new Date();
                      const start = event.date_start ? new Date(event.date_start) : null;
                      const end = event.date_end ? new Date(event.date_end) : false;
                      const isLive = start && !end && now >= start && now >= start;
                      
                      if (isLive && !end) {
                        return <>
                          <span className="text-xs font-bold text-red-600 mb-1 flex items-center gap-1"><GoDotFill className="inline-block" color="red" size={14}/> LIVE</span>
                          <span className="text-lg font-bold text-blue-900">{Array.isArray(event.score) && event.score.length === 2 ? `${event.score[0] ?? 0} : ${event.score[1] ?? 0}` : '-'}</span>
                        </>;
                      } else if (end) {
                        return (
                          <>
                            <span className="text-xs font-bold text-gray-600 mb-1">Закончен</span>
                            <span className="text-lg font-bold text-blue-900">{Array.isArray(event.score) && event.score.length === 2 ? `${event.score[0] ?? 0} : ${event.score[1] ?? 0}` : '-'}</span>
                          </>
                        );
                      }
                      return <>
                        <span className="text-lg font-bold text-blue-900 mb-1">{start ? start.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : '-'}</span>
                        <span className="text-xs text-blue-500">{start && start.toLocaleDateString() === now.toLocaleDateString() ? 'Сегодня' : start ? start.toLocaleDateString() : '-'}</span>
                      </>;
                      
                    })()}
                  </div>
                  <div className="flex flex-col items-center w-16">
                    <img src={event.second_team?.icon_path} alt={event.second_team?.name} className="w-10 h-10 rounded-full bg-white object-contain mb-1" />
                    <span className="text-xs font-semibold text-blue-900 text-center truncate w-full">{event.second_team?.name}</span>
                  </div>
                </div>
                {/* Коэффициенты */}
                <div className="flex items-center justify-between gap-2 px-3 pb-2">
                  <button
                    type="button"
                    className="flex flex-col items-center w-1/3 bg-blue-200 hover:bg-blue-300 rounded-lg py-1 transition-colors"
                    onClick={e => {
                      e.stopPropagation();
                      window.location.href = `/bet?match=${event.id}&outcome=1`;
                    }}
                  >
                    <span className="text-xs text-blue-400">1</span>
                    <span className="font-bold text-blue-900 text-base">{odds.outcomes[0].coefficient ?? '-'}</span>
                  </button>
                  <button
                    type="button"
                    className="flex flex-col items-center w-1/3 bg-blue-200 hover:bg-blue-300 rounded-lg py-1 transition-colors"
                    onClick={e => {
                      e.stopPropagation();
                      window.location.href = `/bet?match=${event.id}&outcome=X`;
                    }}
                  >
                    <span className="text-xs text-blue-400">X</span>
                    <span className="font-bold text-blue-900 text-base">-</span>
                  </button>
                  <button
                    type="button"
                    className="flex flex-col items-center w-1/3 bg-blue-200 hover:bg-blue-300 rounded-lg py-1 transition-colors"
                    onClick={e => {
                      e.stopPropagation();
                      window.location.href = `/bet?match=${event.id}&outcome=2`;
                    }}
                  >
                    <span className="text-xs text-blue-400">2</span>
                    <span className="font-bold text-blue-900 text-base">{odds.outcomes[1].coefficient ?? '-'}</span>
                  </button>
                </div>
              </Link>
            );
          })}
        </div>
      )}
    </div>
  );
});

export default TopEvents;
