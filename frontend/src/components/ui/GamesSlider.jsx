import { useEffect } from 'react';
import { observer } from 'mobx-react-lite';
import { gamesStore } from '../../stores/games';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay } from 'swiper/modules';
import 'swiper/css';

const GamesSlider = observer(() => {
  useEffect(() => {
    gamesStore.fetchGames();
  }, []);

  if (gamesStore.loading) return <div className="text-center py-8">Загрузка игр...</div>;
  if (gamesStore.error) return <div className="text-center text-red-400 py-8">{gamesStore.error}</div>;
  if (!gamesStore.games.length) return <div className="text-center py-8">Нет игр</div>;

  return (
    <div className="container mx-auto px-4 w-full rounded-2xl ">
        <h2 className='mb-4'>
            <span className="text-2xl md:text-2xl font-bold text-black">Киберспорт</span>
        </h2>
      <Swiper
        modules={[Autoplay]}
        autoplay={{ delay: 4000, disableOnInteraction: false }}
        slidesPerView={2}
        spaceBetween={24}
        breakpoints={{
          640: { slidesPerView: 3 },
          1024: { slidesPerView: 4 },
        }}
        loop={gamesStore.games.length > 4}
        className="w-full"
      >
        {gamesStore.games.map((game) => (
          <SwiperSlide key={game.id}>
            <div className="flex flex-col items-center justify-between bg-gradient-to-br from-[#e0e0e0] via-[#bdbdbd] to-[#757575] rounded-2xl h-30 w-46 shadow-lg p-3">
              <div className="w-12 h-12 rounded-xl flex items-center justify-center overflow-hidden mb-2">
                <img src={game.icon_path} alt={game.name} className="object-contain w-full h-full" />
              </div>
              <div className="text-base font-bold text-white text-center truncate w-full">{game.name}</div>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
});

export default GamesSlider;
