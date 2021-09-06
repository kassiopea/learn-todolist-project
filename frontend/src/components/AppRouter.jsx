import React from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';
import {privateRouters, publicRouters} from '../router';
import { getCookie } from '../_helpers';

const AppRouter = () => {
    // заменить на получение данных из куки
    const isCSRFToken = getCookie('csrf_access_token')

    return (
        isCSRFToken
        ?
        <Switch>
            {privateRouters.map(route => 
                
                <Route
                    component={route.component}
                    path={route.path}
                    exact={route.exact}
                    key={route.path}
                />
            )}
            <Redirect from="/" to="/home"/>
        </Switch>
        
        :
        <Switch>
            {publicRouters.map(route => 
                <Route
                    component={route.component}
                    path={route.path}
                    exact={route.exact}
                    key={route.path}
                />
            )}
            <Redirect from="/home" to="/"/>
        </Switch>
    )
}

export default AppRouter;