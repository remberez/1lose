import ScrollBanner from '../components/ui/ScrollBanner';
import GamesSlider from '../components/ui/GamesSlider';
import TopEvents from '../components/ui/TopEvents';

const Home = () => (
  <div className="flex flex-col gap-8">
    <ScrollBanner />
    <div className="container mx-auto bg-white rounded-2xl shadow-lg p-6">
        <GamesSlider />
        <TopEvents />
    </div>
  </div>
);

export default Home;
