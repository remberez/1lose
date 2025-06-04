import React, { useRef, useState } from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay } from 'swiper/modules';
import 'swiper/css';
import { FiChevronLeft, FiChevronRight } from 'react-icons/fi';

const banners = [
	{
		title: 'Добро пожаловать в 1lose!',
		subtitle: 'Лучшие турниры и лотереи для настоящих киберспортсменов.',
		button: 'Зарегистрироваться',
	},
	{
		title: 'Участвуй в турнирах',
		subtitle: 'Проверь свои силы и выиграй крутые призы!',
		button: 'Сделать ставку',
	},
	{
		title: 'Наши клубы по всей стране',
		subtitle: 'Присоединяйся к сообществу и находи новых друзей.',
		button: 'Найти клуб',
	},
	{
		title: 'Статистика и результаты',
		subtitle: 'Следи за результатами и анализируй статистику матчей.',
		button: 'Смотреть статистику',
	},
];

const ScrollBanner = () => {
	const swiperRef = useRef(null);
	const [active, setActive] = useState(0);

	const handlePrev = () => {
		if (swiperRef.current) swiperRef.current.slidePrev();
	};
	const handleNext = () => {
		if (swiperRef.current) swiperRef.current.slideNext();
	};

	return (
		<div className="w-full relative">
			<Swiper
				modules={[Autoplay]}
				autoplay={{ delay: 3500, disableOnInteraction: false }}
				loop={true}
				onSwiper={(sw) => (swiperRef.current = sw)}
				onSlideChange={(sw) => setActive(sw.realIndex)}
				className="shadow-lg w-full"
			>
				{banners.map((banner, idx) => (
					<SwiperSlide key={idx}>
						<div className="bg-blue-800 px-6 py-12 min-h-[260px] md:min-h-[300px] w-full">
							<div className="container mx-auto text-center flex items-center justify-between">
                                {/* Левая часть: текст и кнопки */}
                                <div className="flex flex-col justify-center h-full text-left max-w-[60%] w-full">
                                    <div className="text-2xl md:text-4xl font-extrabold mb-3 text-white leading-tight">
                                        {banner.title}
                                    </div>
                                    <div className="text-base md:text-xl text-blue-100 mb-24">
                                        {banner.subtitle}
                                    </div>
                                    <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded-lg text-base md:text-lg w-fit mb-8 transition-colors">
                                        {banner.button}
                                    </button>
                                    <div className="flex items-center gap-4 mt-auto">
                                        <button
                                            className="w-10 h-10 flex items-center justify-center rounded-full bg-blue-700 hover:bg-blue-900 text-white text-xl transition-colors"
                                            onClick={handlePrev}
                                            aria-label="Назад"
                                        >
                                            <FiChevronLeft />
                                        </button>
                                        <button
                                            className="w-10 h-10 flex items-center justify-center rounded-full bg-blue-700 hover:bg-blue-900 text-white text-xl transition-colors"
                                            onClick={handleNext}
                                            aria-label="Вперёд"
                                        >
                                            <FiChevronRight />
                                        </button>
                                        <span className="ml-4 text-blue-100 text-base select-none">
                                            {active + 1}/{banners.length}
                                        </span>
                                    </div>
                                </div>
                                {/* Правая часть: картинка */}
                                <div className="w-24 h-24 md:w-40 md:h-40 bg-blue-900 rounded-xl flex items-center justify-center">
                                    {/* Здесь будет ваша картинка */}
                                </div>
                            </div>
						</div>
					</SwiperSlide>
				))}
			</Swiper>
		</div>
	);
};

export default ScrollBanner;
