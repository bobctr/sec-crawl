/// <reference types="Cypress" />

context('Set up context', function () {

    beforeEach(function () {
        cy.fixture('newscollection').as('newsList');
        cy.server();  // enable response stubbing
        cy.route('get', '**/news', 'fixture:newscollection.json').as('fakefetch');
    })

    describe('Default content', () => {

        it('Visit the app', () => {         
            cy.visit('/');
            // wait for fake fetch
            cy.wait('@fakefetch');
        });

        it('Check title', () => {
            cy.contains('sec-crawl-news');
        });

        it('Check search bar', () => {
            // focus
            cy.get('#searchbar').click();
            cy.get('#searchbar').focused();

            //icon    
            cy.get('#searchbar').get('svg');

        });
    });

    describe('Mock view', () => {

        it('Check first news', () => {
            cy.get('@newsList').then((newslist) => {
                const firstNews = newslist._items[0];

                cy.get('.news-title').contains(firstNews.title);
                cy.get('.news-date').contains(firstNews.date);
                cy.get('.news-website').contains(firstNews.website);
                cy.get('.news-image').should('have.css', 'background-image', 
                'url("' + firstNews.image + '")');

            });
        });

        it('Check news count', () => {
            cy.get('@newsList').then((newslist) => {
                cy.get('.news-entry').should('have.length', newslist._items.length)
            });
        });

    });
});