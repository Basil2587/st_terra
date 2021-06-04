import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/app/App';
import {BrowserRouter as Router} from 'react-router-dom';
// import ErrorBoundry from './components/error-boundry';

document.body.style.backgroundColor = "#E5E5E5";


ReactDOM.render(
    <Router>
      <App />
    </Router>,
  document.getElementById('root')
);





// import React, {useEffect, useState} from 'react';
// // import AppHeader from '../../appHeader/appHeader';
// import plus from '../../../img/plus.svg';

// const ListItem = ({toggleList,  data, img}) => {

//     const [items, setItems] = useState([]);
//     // const [loading, setLoading] = useState(true);

//     useEffect(() => {
//         setItems([data])
        
//         // setLoading(!loading)
//     }, [data])

//     const [checkbox, setCheckbox] = useState(0);

//     const handleInputChange = (event) => {
//         const target = event.target;
//         // const index = data.findIndex((point) => point.id === target.id);
//         // console.log(target.id)
//         // data = [...data.slice(0, target.id), ...data.slice(target.id + 1)];

//         // console.log(target.id)
//         // const index = data.findIndex((point) => point.id === target.id);
//         // setItems([...data.slice(0, index), ...data.slice(index + 1)])

//         target.checked ? setCheckbox(checkbox + 1) : setCheckbox(checkbox - 1);
//     }

//     if(!data) {
//         return (
//             <div>
//                 <h1>error</h1>
//             </div>
//         )
//     }


//     return (
//         <div className='wrraper'>
//             <div className="d-flex flex-column scroll bg-white">
//                 <div className="overflow">
//                     <div className="name_plus">
//                         <span className="name-title" href="">{'sdf'}</span>
//                         <div onClick={toggleList}><img className='add' src={plus} alt="add"/></div>
//                     </div>
//                     <div className="rating">
//                         <p className="number">{checkbox}/'fse'</p>
//                     </div> 
//                         {
//                             items.map((itemm, index) => {
//                                 console.log(itemm)
//                                 const {data} = itemm;
//                                 console.log(data)
//                                 return (
//                                         <label className="checkbox d-flex" key={index}>
//                                             <input onChange={handleInputChange} id={index} type="checkbox" />
//                                             <p>{itemm}</p>
//                                         </label>
//                                     )
//                             })
//                         }

//                 </div>
//                 <div className="exit-btn btn1">
//                     <button className="btnn" type="btn" name="exit">Показать завершенные</button>
//                 </div>
//             </div>
//             <div className="wrapper__img-list bg-white">
//                 {

//                     img ? <img className="img-list" src={img}/> : null
//                 }
//             </div>
//         </div>
//     );
// }





// export default ListItem; 