import Navbar from'../navbar/navbar';
import AppHeader from '../appHeader/appHeader';
import '@fortawesome/fontawesome-free/css/all.min.css'; import
'bootstrap-css-only/css/bootstrap.min.css'; import
'mdbreact/dist/css/mdb.css';
import {Route} from 'react-router-dom';
import ListPage from '../pages/listPage/listPage.js';
import ResultsPage from '../pages/resultsPage/results';
import '../../index.css';


function App() {
  return (
    <div className="App" >
        <AppHeader/>
      <div className="d-flex">
      <Navbar/>
      <Route path='/list' component={ListPage}/>
      <div className="result-content">
        <Route path='/results' component={ResultsPage}/>
      </div>
      </div>
  
    </div>
  );
}

export default App;
