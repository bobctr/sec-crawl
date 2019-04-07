/// <reference types="Cypress" />

context('Set up context', function () {

    beforeEach(function () {
        cy.fixture('newscollection').as('newsList');
        cy.server();  // enable response stubbing
        cy.route('get', '**', 'fixture:newscollection.json').as('fakefetch');
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
                cy.get('.news-title').first().contains(firstNews.title);
                cy.get('.news-date').first().contains(firstNews.date);
                cy.get('.news-website').first().contains(firstNews.website);
                cy.get('.news-image').first().should('have.css', 'background-image', 
                'url("' + firstNews.image + '")');
                cy.get('a').first().should("have.attr", "href", firstNews._id);
                cy.get('.expand-icon').first().click();
                cy.get('.news-text').first().should('be.visible');
            });
        });

        it('Check news count', () => {
            cy.get('@newsList').then((newslist) => {
                cy.get('.news-entry').should('have.length', newslist._items.length)
            });
        });

    });

    describe('Search news', () => {

        it('Type in search bar', () => {
            cy.get('input').type('bug');
        });
        
        it('Check news count', () => {
            cy.get('.news-entry').should('have.length', 2);
        });

        it('Check filter', () => {
            cy.get('a').eq(0).should('have.attr', 'href',
                'https://thehackernews.com/2019/04/apache-web-server-security.html'
            );
            cy.get('a').eq(1).should('have.attr', 'href',
                'https://www.wired.com/story/huawei-threat-isnt-backdoors-its-bugs/'
            );

        });
    });
});