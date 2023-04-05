CREATE TABLE [dbo].[Customer] (
    [Phone_Number]   CHAR (20)  NULL,
    [Customer_Id]    INT        NOT NULL,
    [First_Name]     CHAR (50)  NULL,
    [Zip_Code_Ext]   CHAR (4)   NULL,
    [Last_Name]      CHAR (50)  NULL,
    [Street_Address] CHAR (100) NULL,
    [Name]           CHAR (100) NULL,
    [Email]          CHAR (100) NULL,
    [Zip_Code]       CHAR (5)   NULL,
    CONSTRAINT [PK_Customer] PRIMARY KEY CLUSTERED ([Customer_Id] ASC),
    CONSTRAINT [FK_Customer_Zip_Code] FOREIGN KEY ([Zip_Code]) REFERENCES [dbo].[Zip_Code] ([Zip_Code])
);


GO

CREATE TABLE [dbo].[Zip_Code] (
    [State_Abbr] CHAR (2)        NULL,
    [City]       CHAR (50)       NULL,
    [Longitude]  DECIMAL (10, 7) NULL,
    [Zip_Code]   CHAR (5)        NOT NULL,
    [Latitude]   DECIMAL (10, 7) NULL,
    CONSTRAINT [PK_Zip_Code] PRIMARY KEY CLUSTERED ([Zip_Code] ASC),
    CONSTRAINT [FK_Zip_Code_State] FOREIGN KEY ([State_Abbr]) REFERENCES [dbo].[State] ([State_Abbr])
);


GO

CREATE TABLE [dbo].[Item_Type] (
    [Item_Type]    CHAR (20) NULL,
    [Item_Type_ID] INT       NOT NULL,
    CONSTRAINT [PK_Item_Type] PRIMARY KEY CLUSTERED ([Item_Type_ID] ASC)
);


GO

CREATE TABLE [dbo].[Producer] (
    [Producer_Name] CHAR (100) NULL,
    [Producer_ID]   INT        NOT NULL,
    CONSTRAINT [PK_Producer] PRIMARY KEY CLUSTERED ([Producer_ID] ASC)
);


GO

CREATE TABLE [dbo].[Album] (
    [Album_Id]        INT             NOT NULL,
    [Album_Name]      CHAR (100)      NULL,
    [Production_Cost] DECIMAL (18, 2) NULL,
    [Band_Id]         INT             NOT NULL,
    [Release_Date]    DATETIME        NULL,
    CONSTRAINT [PK_Album] PRIMARY KEY CLUSTERED ([Album_Id] ASC),
    CONSTRAINT [FK_Album_Band] FOREIGN KEY ([Band_Id]) REFERENCES [dbo].[Band] ([Band_Id]),
    CONSTRAINT [FK_Album_Item] FOREIGN KEY ([Album_Id]) REFERENCES [dbo].[Item] ([Item_ID])
);


GO

CREATE TABLE [dbo].[Customer_Profile] (
    [Profile_ID]     INT      NOT NULL,
    [Birthdate]      DATETIME NULL,
    [Favorite_Album] INT      NULL,
    [Favorite_Song]  INT      NULL,
    [Favorite_Band]  INT      NULL,
    [Gender]         CHAR (1) NULL,
    CONSTRAINT [PK_Customer_Profile] PRIMARY KEY CLUSTERED ([Profile_ID] ASC),
    CONSTRAINT [FK_Customer_Profile_Album] FOREIGN KEY ([Favorite_Album]) REFERENCES [dbo].[Album] ([Album_Id]),
    CONSTRAINT [FK_Customer_Profile_Band] FOREIGN KEY ([Favorite_Band]) REFERENCES [dbo].[Band] ([Band_Id]),
    CONSTRAINT [FK_Customer_Profile_Customer] FOREIGN KEY ([Profile_ID]) REFERENCES [dbo].[Customer] ([Customer_Id]),
    CONSTRAINT [FK_Customer_Profile_Song] FOREIGN KEY ([Favorite_Song]) REFERENCES [dbo].[Song] ([Song_Id])
);


GO

CREATE TABLE [dbo].[Band_Genre] (
    [Genre_Id] INT NOT NULL,
    [Band_Id]  INT NOT NULL,
    CONSTRAINT [PK_Band_Genre] PRIMARY KEY CLUSTERED ([Genre_Id] ASC, [Band_Id] ASC),
    CONSTRAINT [FK_Band_Genre_Band] FOREIGN KEY ([Band_Id]) REFERENCES [dbo].[Band] ([Band_Id]),
    CONSTRAINT [FK_Band_Genre_Genre] FOREIGN KEY ([Genre_Id]) REFERENCES [dbo].[Genre] ([Genre_ID])
);


GO

CREATE TABLE [dbo].[Order_Detail] (
    [Line_Number] INT             NOT NULL,
    [Quantity]    INT             NULL,
    [Item_ID]     INT             NULL,
    [Order_Id]    INT             NOT NULL,
    [Unit_Price]  DECIMAL (18, 2) NULL,
    CONSTRAINT [PK_Order_Detail] PRIMARY KEY CLUSTERED ([Line_Number] ASC, [Order_Id] ASC),
    CONSTRAINT [FK_Order_Detail_Item] FOREIGN KEY ([Item_ID]) REFERENCES [dbo].[Item] ([Item_ID]),
    CONSTRAINT [FK_Order_Detail_Order_Header] FOREIGN KEY ([Order_Id]) REFERENCES [dbo].[Order_Header] ([Order_Id])
);


GO

CREATE TABLE [dbo].[Contract] (
    [Live_Rev_Pct]  DECIMAL (18, 2) NULL,
    [Band_Id]       INT             NULL,
    [Contract_Id]   INT             NOT NULL,
    [Album_Count]   INT             NULL,
    [Agent_Id]      INT             NULL,
    [End_Date]      DATETIME        NULL,
    [Begin_Date]    DATETIME        NULL,
    [Live_Count]    INT             NULL,
    [Album_Rev_Pct] DECIMAL (18, 2) NULL,
    CONSTRAINT [PK_Contract] PRIMARY KEY CLUSTERED ([Contract_Id] ASC),
    CONSTRAINT [FK_Contract_Agent] FOREIGN KEY ([Agent_Id]) REFERENCES [dbo].[Agent] ([Agent_Id]),
    CONSTRAINT [FK_Contract_Band] FOREIGN KEY ([Band_Id]) REFERENCES [dbo].[Band] ([Band_Id])
);


GO

CREATE TABLE [dbo].[Video] (
    [Producer_ID] INT        NULL,
    [Video_Name]  CHAR (100) NULL,
    [Video_ID]    INT        NOT NULL,
    CONSTRAINT [PK_Video] PRIMARY KEY CLUSTERED ([Video_ID] ASC),
    CONSTRAINT [FK_Video_Item] FOREIGN KEY ([Video_ID]) REFERENCES [dbo].[Item] ([Item_ID]),
    CONSTRAINT [FK_Video_Producer] FOREIGN KEY ([Producer_ID]) REFERENCES [dbo].[Producer] ([Producer_ID])
);


GO

CREATE TABLE [dbo].[Item] (
    [Item_Description] CHAR (200) NULL,
    [Item_Type_ID]     INT        NULL,
    [Item_ID]          INT        NOT NULL,
    CONSTRAINT [PK_Item] PRIMARY KEY CLUSTERED ([Item_ID] ASC),
    CONSTRAINT [FK_Item_Item_Type] FOREIGN KEY ([Item_Type_ID]) REFERENCES [dbo].[Item_Type] ([Item_Type_ID])
);


GO

CREATE TABLE [dbo].[Person] (
    [Street_Address] CHAR (100) NULL,
    [Person_Id]      INT        NOT NULL,
    [Phone_Number]   CHAR (20)  NULL,
    [Zip_Code]       CHAR (5)   NULL,
    [Last_Name]      CHAR (50)  NULL,
    [First_Name]     CHAR (50)  NULL,
    [Email]          CHAR (100) NULL,
    [Zip_Code_Ext]   CHAR (4)   NULL,
    CONSTRAINT [PK_Person] PRIMARY KEY CLUSTERED ([Person_Id] ASC),
    CONSTRAINT [FK_Person_Zip_Code] FOREIGN KEY ([Zip_Code]) REFERENCES [dbo].[Zip_Code] ([Zip_Code])
);


GO

CREATE TABLE [dbo].[Agent] (
    [Hire_Date]         DATETIME        NULL,
    [Agent_Status_Code] CHAR (1)        NULL,
    [Salary]            DECIMAL (18, 2) NULL,
    [Agent_Id]          INT             NOT NULL,
    [Commission]        DECIMAL (5, 4)  NULL,
    CONSTRAINT [PK_Agent] PRIMARY KEY CLUSTERED ([Agent_Id] ASC),
    CONSTRAINT [FK_Agent_Agent] FOREIGN KEY ([Agent_Id]) REFERENCES [dbo].[Person] ([Person_Id])
);


GO

CREATE TABLE [dbo].[Member_Instrument] (
    [Instrument_Id] INT NOT NULL,
    [Member_Id]     INT NOT NULL,
    CONSTRAINT [PK_Member_Instrument] PRIMARY KEY CLUSTERED ([Instrument_Id] ASC, [Member_Id] ASC),
    CONSTRAINT [FK_Member_Instrument_Band_Member] FOREIGN KEY ([Member_Id]) REFERENCES [dbo].[Band_Member] ([Member_Id]),
    CONSTRAINT [FK_Member_Instrument_Instrument] FOREIGN KEY ([Instrument_Id]) REFERENCES [dbo].[Instrument] ([Instrument_Id])
);


GO

CREATE TABLE [dbo].[Band_Member] (
    [Member_Status_Code] CHAR (1) NULL,
    [Join_Date]          DATETIME NULL,
    [Member_Id]          INT      NOT NULL,
    [Band_Id]            INT      NULL,
    CONSTRAINT [PK_Band_Member] PRIMARY KEY CLUSTERED ([Member_Id] ASC),
    CONSTRAINT [FK_Band_Member_Band] FOREIGN KEY ([Band_Id]) REFERENCES [dbo].[Band] ([Band_Id]),
    CONSTRAINT [FK_Band_Member_Person] FOREIGN KEY ([Member_Id]) REFERENCES [dbo].[Person] ([Person_Id])
);


GO

CREATE TABLE [dbo].[Instrument] (
    [Instrument_Name] CHAR (50) NULL,
    [Instrument_Id]   INT       NOT NULL,
    CONSTRAINT [PK_Instrument] PRIMARY KEY CLUSTERED ([Instrument_Id] ASC)
);


GO

CREATE TABLE [dbo].[Performance] (
    [Band_Id]          INT             NULL,
    [Revenue]          DECIMAL (18, 2) NULL,
    [Performance_Date] DATETIME        NULL,
    [Venue_Id]         INT             NULL,
    [Performance_Id]   INT             NOT NULL,
    [Agent_Id]         INT             NULL,
    CONSTRAINT [PK_Performance] PRIMARY KEY CLUSTERED ([Performance_Id] ASC),
    CONSTRAINT [FK_Performance_Agent] FOREIGN KEY ([Agent_Id]) REFERENCES [dbo].[Agent] ([Agent_Id]),
    CONSTRAINT [FK_Performance_Band] FOREIGN KEY ([Band_Id]) REFERENCES [dbo].[Band] ([Band_Id]),
    CONSTRAINT [FK_Performance_Venue] FOREIGN KEY ([Venue_Id]) REFERENCES [dbo].[Venue] ([Venue_Id])
);


GO

CREATE TABLE [dbo].[Venue] (
    [Venue_Id]       INT        NOT NULL,
    [Zip_Code_Ext]   CHAR (4)   NULL,
    [Street_Address] CHAR (100) NULL,
    [Zip_Code]       CHAR (5)   NULL,
    [Venue_Name]     CHAR (100) NULL,
    [Contact_Phone]  CHAR (20)  NULL,
    CONSTRAINT [PK_Venue] PRIMARY KEY CLUSTERED ([Venue_Id] ASC),
    CONSTRAINT [FK_Venue_Zip_Code] FOREIGN KEY ([Zip_Code]) REFERENCES [dbo].[Zip_Code] ([Zip_Code])
);


GO

CREATE TABLE [dbo].[Song] (
    [Sequence]         INT        NULL,
    [Song_Id]          INT        NOT NULL,
    [Duration_Seconds] INT        NULL,
    [Album_Id]         INT        NULL,
    [Song_Name]        CHAR (100) NULL,
    CONSTRAINT [PK_Song] PRIMARY KEY CLUSTERED ([Song_Id] ASC),
    CONSTRAINT [FK_Song_Album] FOREIGN KEY ([Album_Id]) REFERENCES [dbo].[Album] ([Album_Id]),
    CONSTRAINT [FK_Song_Item] FOREIGN KEY ([Song_Id]) REFERENCES [dbo].[Item] ([Item_ID])
);


GO

CREATE TABLE [dbo].[Order_Header] (
    [Order_Source_Id] INT             NULL,
    [Order_Id]        INT             NOT NULL,
    [Customer_Id]     INT             NULL,
    [Subtotal_Amount] DECIMAL (18, 2) NULL,
    [Promise_Date]    DATETIME        NULL,
    [Order_Date]      DATETIME        NULL,
    [Total_Amount]    DECIMAL (18, 2) NULL,
    [Tax_Amount]      DECIMAL (18, 2) NULL,
    CONSTRAINT [PK_Order_Header] PRIMARY KEY CLUSTERED ([Order_Id] ASC),
    CONSTRAINT [FK_Order_Header_Customer] FOREIGN KEY ([Customer_Id]) REFERENCES [dbo].[Customer] ([Customer_Id]),
    CONSTRAINT [FK_Order_Header_Order_Source] FOREIGN KEY ([Order_Source_Id]) REFERENCES [dbo].[Order_Source] ([Order_Source_Id])
);


GO

CREATE TABLE [dbo].[Customer_Genre] (
    [Genre_ID]   INT NOT NULL,
    [Profile_ID] INT NOT NULL,
    CONSTRAINT [PK_Customer_Genre] PRIMARY KEY CLUSTERED ([Genre_ID] ASC, [Profile_ID] ASC),
    CONSTRAINT [FK_Customer_Genre_Customer_Genre] FOREIGN KEY ([Genre_ID]) REFERENCES [dbo].[Genre] ([Genre_ID])
);


GO

CREATE TABLE [dbo].[Band] (
    [Band_Id]            INT        NOT NULL,
    [Band_Status_Code]   CHAR (1)   NULL,
    [Band_Name]          CHAR (100) NULL,
    [ZIP_Code]           CHAR (5)   NULL,
    [Primary_Contact_Id] INT        NOT NULL,
    [Formation_Date]     DATETIME   NULL,
    CONSTRAINT [PK_Band] PRIMARY KEY CLUSTERED ([Band_Id] ASC),
    CONSTRAINT [FK_Band_Person] FOREIGN KEY ([Primary_Contact_Id]) REFERENCES [dbo].[Person] ([Person_Id]),
    CONSTRAINT [FK_Band_Zip_Code] FOREIGN KEY ([ZIP_Code]) REFERENCES [dbo].[Zip_Code] ([Zip_Code])
);


GO

CREATE TABLE [dbo].[Genre] (
    [Genre]    CHAR (50) NULL,
    [Genre_ID] INT       NOT NULL,
    CONSTRAINT [PK_Genre] PRIMARY KEY CLUSTERED ([Genre_ID] ASC)
);


GO

CREATE TABLE [dbo].[State] (
    [State_Name] CHAR (20) NULL,
    [State_Abbr] CHAR (2)  NOT NULL,
    CONSTRAINT [PK_State] PRIMARY KEY CLUSTERED ([State_Abbr] ASC)
);


GO

CREATE TABLE [dbo].[Order_Source] (
    [Source_Description] CHAR (200) NULL,
    [Source_Name]        CHAR (100) NULL,
    [Order_Source_Id]    INT        NOT NULL,
    CONSTRAINT [PK_Order_Source] PRIMARY KEY CLUSTERED ([Order_Source_Id] ASC)
);
GO
