SELECT tt.topic, 
	tt.term, 
	tt.weight, 
	dt.docname,
    dt.proportion
FROM linkedTopicDB2.neg_reviews_topic_terms tt, linkedTopicDB2.neg_reviews_doc_topics dt
WHERE tt.topic = dt.topic
ORDER BY topic ASC;